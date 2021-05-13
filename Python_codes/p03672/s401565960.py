s = input()
n = len(s)

for i in range(2, n, 2):
  flag = 1
  for j in range(n-i-1, int((n-i)/2-1),-1):
    if s[j] != s[j-int((n-i)/2)]:
      flag = 0
      break
  if flag == 1:
    break
    
print(n-i)
