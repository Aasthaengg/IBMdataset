a,b,k=map(int,input().split())
n=a*b+1
ans=[0]*n
for i in range(a+1):
    for j in range(b+1):
        ans[a*j+b*i-2*i*j]=1
print("Yes" if ans[k] else "No")