n = int(input())
s = input()

R = []
G = []
list = [0]*n
number_B = 0
for i in range(n):
  if s[i] == 'R':
    R.append(i)
  elif s[i] == 'G':
    G.append(i)
  else:
    list[i] = 1
    number_B += 1
    

ans = 0
for i in R:
  for j in G:
    minus = 0
    if i < j:
      if 2*i-j >= 0 and list[2*i-j] == 1:
        minus += 1   
      if (i+j)%2 == 0 and list[int((i+j)/2)] == 1:
        minus += 1      
      if 2*j-i<n and list[2*j-i] == 1:
        minus += 1
    else:
      if 2*j-i >= 0 and list[2*j-i] == 1:
        minus += 1   
      if (i+j)%2 == 0 and list[int((i+j)/2)] == 1:
        minus += 1      
      if 2*i-j<n and list[2*i-j] == 1:
        minus += 1
    ans += (number_B-minus)
    
print(ans)
