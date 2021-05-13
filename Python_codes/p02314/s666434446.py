n, m = map(int, input().split())
coin = sorted(list(map(int, input().split())))
T = [0]+[float('inf')]*n
for i in range(m):
    for j in range(coin[i], n+1):
        T[j] = min(T[j], T[j-coin[i]]+1)
print(T[-1])