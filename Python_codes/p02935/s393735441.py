N=int(input())
v=list(map(int,input().split()))
v.sort()
ans=0
for i in range(N):
    ans+=(v[i])/(2**(N-i))
ans+=(v[0])/(2**N)
print(ans)