n,m = map(int, input().split())
C = list(map(int, input().split()))
inf = float("inf")
T = [inf for i in range(n+1)]
T[0] = 0

for i in range(m):
    for j in range(C[i], n+1):
        T[j] = min(T[j], T[j - C[i]] + 1)

print(str(T[n]))