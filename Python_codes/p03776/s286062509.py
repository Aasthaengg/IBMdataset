N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)

C = [[1 for k in range(n + 1)] for n in range(N + 1)]
for n in range(2, N + 1):
    for k in range(1, n):
        C[n][k] = C[n - 1][k] + C[n - 1][k - 1]

x = v[A - 1]
l = 0
while v[l] != x:
    l += 1
r = l + 1
while r < N and v[r] == x:
    r += 1


count = 0
for i in range(A, min(B, r) + 1):
    if sum(v[:A]) * i == sum(v[:i]) * A:
        count += C[r - l][i - l]
print(sum(v[:A]) / A)
print(count)