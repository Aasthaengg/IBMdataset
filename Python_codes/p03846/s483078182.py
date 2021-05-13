from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))
MOD = 10 ** 9 + 7

if N % 2:
    if A == Counter((i + 1) // 2 * 2 for i in range(N)):
        print(pow(2, (N - 1) // 2, MOD))
    else:
        print(0)
else:
    if A == Counter(i // 2 * 2 + 1 for i in range(N)):
        print(pow(2, N // 2, MOD))
    else:
        print(0)
