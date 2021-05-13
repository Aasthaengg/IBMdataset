N = int(input())
P = sorted([int(input()) for _ in range(N)], reverse=True)
ans = sum(P) - P[0] // 2
print(ans)
