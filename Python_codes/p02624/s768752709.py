N=int(input())
ans=0
for j in range(1,N+1):
    for k in range(1,N//j+1):
        ans+=k*j
print(ans)