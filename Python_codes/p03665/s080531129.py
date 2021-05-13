import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, P = map(int, input().split())
A = list(map(int, input().split()))

n = [0] * 2

for a in A:
    n[a % 2] += 1


if P == 1:
    ans = 0
    for i in range(1, n[1]+1, 2):
        ans += comb(n[1], i)
    ans *= 2 ** n[0]
else:
    ans = 0
    for i in range(0, n[1]+1, 2):
        if i == 0:
            ans += 1
        else:
            ans += comb(n[1], i)
    ans *= 2 ** n[0]
    #ans += 1

print(ans)