def digitsum(N): # intで渡す
    return sum(int(s) for s in str(N))
ans=INF=9*10
N=int(input())
for a in range(1,N):
    b=N-a
    ans=min(digitsum(a)+digitsum(b),ans)
print(ans)