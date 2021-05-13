n,k=map(int,input().split())
a=list(map(int,input().split()))
m=10**9+7
s=sum
print(s((((s(a[i]>j for j in a[i:])*(k*(k+1)//2)%m)+(s(a[i]>j for j in a[:i+1])*(k*(k-1)//2)%m))%m) for i in range(n))%m)