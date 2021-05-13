# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_d

from math import ceil, floor

def divisors(N):
    ans = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            if N // i != i:
                ans.append(N // i)
        i += 1
    ans.sort()
    return ans

N = int(input())
fN = divisors(N)

total = 0
for m in fN[1:]:
    m -= 1
    if floor(N / m) == N % m:
        total += m
print(total)