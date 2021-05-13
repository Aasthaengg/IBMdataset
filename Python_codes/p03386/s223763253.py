a,b,k=map(int,input().split())
l1=[i for i in range(a,a+k) if i<=b]
l2=[i for i in range(b,b-k,-1) if i>=a]
ans=sorted(set(l1+l2))
for i in ans:
    print(i)