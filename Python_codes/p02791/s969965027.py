N = int(input())
P = list(map(int, input().split()))

INF = 10 ** 18
A = [0] * N
mn = INF
for i, p in enumerate(P):
    if p < mn:
        mn = p
        A[i] = p
    else:
        A[i] = mn

ans = 0
for i, p in enumerate(P):
    if A[i] >= p:
        ans += 1
print(ans)