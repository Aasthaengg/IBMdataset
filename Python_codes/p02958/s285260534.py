N=int(input())
p=[0]+list(map(int,input().split()))
d=list(range(0,N+1))
err=0
for i in range(N):
    if p[i]!=d[i]:
       err+=1
if err<=2:
    print('YES')
else:
    print('NO')