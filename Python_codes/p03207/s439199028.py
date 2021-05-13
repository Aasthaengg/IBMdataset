N = int(input())
p = [int(input()) for _ in range(N)]
p.sort()
ans = sum(p[:N - 1]) + p[N - 1] // 2
print(ans)
