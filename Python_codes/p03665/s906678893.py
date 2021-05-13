N, P = map(int, input().split())
A = map(int, input().split())

odds, evens = 0, 0

for i in A:
    if i & 1:
        odds += 1
        
    else:
        evens += 1

from math import factorial

if P == 0:
    ans = 0
    fo = factorial(odds)
    for r in range(0, odds + 1, 2):
        ans += fo // (factorial(odds - r) * factorial(r))
    ans *= 2**evens

else:
    ans = 0
    fo = factorial(odds)
    for r in range(1, odds + 1, 2):
        ans += fo // (factorial(odds - r) * factorial(r))

    ans *= 2**evens
print(ans)
