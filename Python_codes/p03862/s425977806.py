
si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
lmsi = lambda: list(map(str, input().split()))
smii = lambda: sorted(map(int, input().split()))

# ----------

N, x = mii()
A = lmii()

ans = 0
for i in range(1, N):
    if A[i] + A[i-1] > x:
        need = A[i] + A[i-1] - x
        ans += need
        if A[i] >= need:
            A[i] -= need
        else:
            A[i-1] = need - A[i]
            A[i] = 0

print(ans)


