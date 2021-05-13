N, K, S = map(int, input().split())
ans = [S]*K + [S+1 if S!=10**9 else 1]*(N-K) 
print(*ans)