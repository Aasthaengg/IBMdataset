N=int(input())
v=list(map(float,input().strip().split()))

v.sort()

ans=v[0]
for n in range(1,N):
    ans=(ans+v[n])/2

print(ans)