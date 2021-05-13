n = int(input())
a = list(map(int, input().split()))

flag = [-1]*n
t = 0
for i in range(n-1):
  if t == 0:
    if a[i] < a[i+1]:
      flag[i] = 0
      t = 1
  elif t == 1:
    if a[i+1] < a[i]:
      flag[i] = 1
      t = 0

if t == 1:
  for i in range(n-1, -1, -1):
    if flag[i] == 0:
      flag[i] == -1
      break
    if a[i] < a[i-1]: continue
    flag[i] = 1
    break
    
ans = 1000
s = 0
for i in range(n):
  if flag[i] == 0:
    s = ans//a[i]
    ans %= a[i]
  elif flag[i] == 1:
    ans += s*a[i]
    s = 0
print(ans)