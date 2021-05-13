n, m = map(int, input().split())
d = list(map(int, input().split()))

T = [50001]*(n+1)
T[0] = 0
for i in range(m):
    for j in range(d[i],n+1):
        T[j] = min(T[j], T[j-d[i]]+1)
print(T[n])
