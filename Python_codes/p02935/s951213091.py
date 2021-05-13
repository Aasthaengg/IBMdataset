N = int(input())
V = list(map(int, input().split()))
V.sort()

ans = 0
for i in range(N - 1):
    m = (V[i] + V[i+1]) / 2
    V[i+1] = m
    ans = m
print(ans)