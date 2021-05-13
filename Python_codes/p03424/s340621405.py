n = int(input())
s = list(input().split())

res = []
ans = 0
for i in s:
  if i not in res:
    res.append(i)
    ans += 1
    
if ans == 3:
  print('Three')
else:
  print('Four')