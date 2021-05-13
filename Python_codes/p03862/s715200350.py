n,x = map(int,input().split())
A = list(map(int,input().split()))
Arev = A[::-1]
ans = 0
if A[0] > x:
    ans += A[0] - x
    A[0] = x
for i in range(1, n):
    if A[i] + A[i-1] > x:
        c = A[i] + A[i-1] - x
        A[i] -= c
        ans += c

ans2 = 0
if Arev[0] > x:
    ans2 += Arev[0] - x
    Arev[0] = x
for i in range(1, n):
    if Arev[i] + Arev[i-1] > x:
        c = Arev[i] + Arev[i-1] - x
        Arev[i] -= c
        ans2 += c

print(min(ans, ans2))