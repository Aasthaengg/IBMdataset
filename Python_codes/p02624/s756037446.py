N=input()
ans=(1+N)*N/2
for skip in range(2,N+1):
    for i in range(skip,N+1,skip):
        ans+=i
print ans
