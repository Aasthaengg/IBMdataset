n,k=map(int,input().split())
*h,=sorted(map(int,input().split()),reverse=1)
for i in range(min(k,n)):
    h[i]=0
print(sum(h))