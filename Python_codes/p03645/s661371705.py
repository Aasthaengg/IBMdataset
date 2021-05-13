N,M=map(int,input().split())
c1=[]
c2=[]
for i in range(M):
    a,b=map(int,input().split())
    if a==1:
        c1.append(b)
    if b==N:
        c2.append(a)
c1=set(c1)
c2=set(c2)
if c1&c2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')