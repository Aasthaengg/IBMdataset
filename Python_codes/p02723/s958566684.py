s = list(input())

sign = 1
if (s[2] == s[3]) and (s[4] == s[5]):
  sign = 0
  
if sign == 0:
  ans = 'Yes'
elif sign == 1:
  ans = 'No'
  
print(ans)