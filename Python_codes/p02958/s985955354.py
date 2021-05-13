N=int(input())
p=list(map(int,input().split()))
q=sorted(p)
a=0
for i in range(N):
    if p[i]!=q[i]:
        a+=1
    if a>2:
        print('NO')
        exit()
if a==0 or a==2:
    print('YES')
else:
    print('NO')