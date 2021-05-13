N=int(input())
p=list(map(int,input().split()))
Q=sorted(p)
count=0
for i in range(N):
    if p[i]!=Q[i]:
        count+=1
if count<=2:
    print('YES')
else:
    print('NO')