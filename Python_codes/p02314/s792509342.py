n, m = map(int, input().split())
c = list(map(int, input().split()))

INF = 10**12

T = [i for i in range(n+1)]

for i in range(m):
    for j in range(1, n+1):
        if j - c[i] >= 0:
            T[j] = min(T[j], T[j - c[i]] + 1)

print(T[n])