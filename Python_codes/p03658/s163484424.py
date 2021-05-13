n,k=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a)

b=sum(a)
for i in range(n-k):
    b-=a[i]

print(b)