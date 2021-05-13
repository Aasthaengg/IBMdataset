
def solve(S):
    N = len(S)
    res = 0
    xa = 0
    bx = 0
    ba = 0

    for s in S:
        if s[-1] == 'A' and s[0] == 'B':
            ba += 1
        else:
            xa += int(s[-1] == 'A')
            bx += int(s[0] == 'B')
        res += s.count('AB')

    if ba == 0:
        return res + min(xa,bx)

    if xa > 0 and bx > 0:
        res += ba + 1
        xa -= 1
        bx -= 1
    elif xa > 0:
        res += ba
        xa -= 1
    elif bx > 0:
        res += ba
        bx -= 1
    else:
        res += ba - 1

    return res + min(xa,bx)

from itertools import permutations
def naive(S):
    
    return max(''.join(x).count('AB') for x in permutations(S))

from random import randrange

# N = 5
# for i in range(100000):
#     print(i)

#     S = [''.join(chr(ord('A')+randrange(3)) for _ in range(3)) for _ in range(N)]

#     r1 = solve(S)
#     r2 = naive(S)
#     if r1 != r2:
#         print(r1,r2)
#         print(S)
#         break

N = int(input())
S = [input() for _ in range(N)]
print(solve(S))