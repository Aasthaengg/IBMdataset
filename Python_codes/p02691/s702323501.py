N = int(input())
A = list(map(int, input().split()))

t = [0] * (N + 1)
ans = 0
for i in range(N):
    sa = i - A[i]
    if sa >= 0:
        ans += t[sa]
    wa = i + A[i]
    if wa < N:
        t[wa] += 1

print(ans)
