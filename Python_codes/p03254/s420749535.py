N, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for a in A[:-1]:
    if x - a >= 0:
        x -= a
        ans += 1
print(ans + (A[-1] == x))
