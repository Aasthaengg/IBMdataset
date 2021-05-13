n,k=map(int,input().split())

i=1
ans=k
while i<n:

    ans=ans*(k-1)
    i+=1

print(ans)