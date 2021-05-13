from collections import Counter

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

N = int(input())
S = []
for _ in range(N):
    string = sorted(input())
    string = "".join(string)
    S.append(string)

S_counter = Counter(S)

ans = 0
for i in S_counter.values():
    if i != 1:
        number = cmb(i, 2)
        ans = ans + number

print(ans)
