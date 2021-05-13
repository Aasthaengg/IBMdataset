s = input()
k = int(input())
sign = 1

num_s = len(list(s))
count = 0
temp_count = 1
count_1 = 0
count_2 = 0

if s[0] != s[-1]:
  for i in range(1,num_s):
    if s[i-1] == s[i]:
      temp_count += 1
    elif s[i-1] != s[i]:
      count += temp_count//2
      temp_count = 1
      
  ans = (count+temp_count//2)*k
  
elif s[0] == s[-1]:
  for i in range(1,num_s):
    if s[i-1] == s[i]:
      temp_count += 1
    elif s[i-1] != s[i]:
      if sign == 1:
        count_1 = temp_count
        sign = 0
      elif sign == 0:
        count += temp_count//2
     
      temp_count = 1

  count_2 = temp_count
  
  ans = count*k + ((count_1 + count_2)//2)*(k-1) + (count_1//2) + (count_2//2)

  if sign == 1:
    ans = (k*num_s)//2
    
if num_s == 1:
  ans = k//2
  
print(ans)