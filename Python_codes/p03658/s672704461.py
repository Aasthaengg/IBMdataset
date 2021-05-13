n,k=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l,reverse=True)
x=0
for j in range(k):
    x+=l[j]
print(x)