import sys
n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))
if n < m:
  # 問題数不足
  print('NO')
  sys.exit()
d.sort()
t.sort()
j=0
for i in range(n):
  if d[i] == t[j]:
    # 一致
    j += 1
  elif d[i] > t[j]:
    print('NO')
    break
  if j == m:
    print('YES')
    break
else:
  print('NO')