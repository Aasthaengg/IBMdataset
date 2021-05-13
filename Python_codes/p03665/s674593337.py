def LI():
    return list(map(int, input().split()))


N, P = LI()
A = LI()
gu = 0
ki = 0
for i in range(N):
    if A[i] % 2 == 0:
        gu += 1
    else:
        ki += 1


if ki == 0:
    if P == 0:
        ans = 2**N
    else:
        ans = 0
else:
    ans = 2**(N-1)
print(ans)