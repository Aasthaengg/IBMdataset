N, M, X = map(int, input().split())
A = list(map(int, input().split()))
m = [0 for _ in range(N+1)]
for a in A:
    m[a] += 1
print(min(sum(m[:X]), sum(m[X:])))