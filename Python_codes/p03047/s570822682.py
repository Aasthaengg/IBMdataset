n,k=map(int,input().split())
l=[i for i in range(1,n+1)]
ans=[]
for i in range(n-k+1):
    ans+=[l[i:k+i]]
print(len(ans))