n = int(input())
p = list(map(int,input().split()))
count=0
pp = sorted(p)
for i in range(n):
  if p[i] != pp[i]:
    count+=1
if count<=2:
  print('YES')
else:
  print('NO')