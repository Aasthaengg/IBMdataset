n,m=map(int,input().split())
A=list(map(int,input().split()))
x=0
if n<sum(A):
    ans=-1
else:
    ans=n-sum(A)
print(ans)