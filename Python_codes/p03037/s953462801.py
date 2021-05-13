L,M=map(int,input().split())
a=[0]*L
x=[]
y=[]
for i in range(M):
    b,c=map(int,input().split())
    x.append(b)
    y.append(c)
if max(x)<=min(y):
    print(-max(x)+min(y)+1)
else:
    print(0)