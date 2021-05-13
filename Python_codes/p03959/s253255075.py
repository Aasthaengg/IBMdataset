N = int(input())
T = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
mod = 10**9 + 7
upT = set()
upA = set()
for i in range(N):
    if i == 0 or T[i - 1] < T[i]:
        upT.add(i)
    if i == N - 1 or A[i] > A[i + 1]:
        upA.add(i)
ans = 1
for i in range(N):
    if i in upT:
        if T[i] > A[i]:
            ans = 0
            break
    elif i in upA:
        if T[i] < A[i]:
            ans = 0
            break
    else:
        ans *= min(T[i], A[i])
        ans %= mod
print(ans)
