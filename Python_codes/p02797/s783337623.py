N,K,S=map(int, input().split())
ans=[S]*K
if S!=10**9:
    add=10**9
else:
    add=10**9-1
ans=ans+[add]*(N-K)
print(*ans)