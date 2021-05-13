n=int(input())
p=list(map(int,input().split()))
pf=sorted(p)
cnt=0
for i in range(n):
  if p[i] > pf[i]:
    cnt+=1
if cnt < 2:
  print('YES')
else:
  print('NO')