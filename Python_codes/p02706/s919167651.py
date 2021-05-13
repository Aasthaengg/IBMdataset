a,b=map(int,input().split())
c=0
d=list(map(int,input().split()))
for i in range(b):
    a-=d[i]
if a<0:
    print(-1)
else:
    print(a)
