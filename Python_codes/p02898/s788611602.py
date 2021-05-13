N,K=map(int,input().split())
h=list(map(int,input().split()))
l=len(h)
x=[False for x in range(l)]
for i in range(l):
    if h[i]>=K:
        x[i]=True
print(x.count(True))  