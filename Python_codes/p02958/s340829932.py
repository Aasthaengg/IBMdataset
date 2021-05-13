N=int(input())
p1=list(map(int,input().split()))
p2=sorted(p1)
count=0
for i in range(N):
  if p1[i]!=p2[i]:count+=1

if count in [0,2]:print('YES')
else:print('NO')