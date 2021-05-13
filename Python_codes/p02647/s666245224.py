n, k = map(int, input().split())

a = list(map(int, input().split()))

def IMOS(a):
    imos = [0]*n
    for i, ai in enumerate(a):
        imos[max(i-ai, 0)] += 1
        if i+ai+1 < n:
            imos[i+ai+1] -= 1
    for i in range(1, n):
        imos[i] += imos[i-1]
    return imos

for _ in range(k):
    if sum(a) == n*n:
        break
    a = IMOS(a)

print(*a)