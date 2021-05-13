from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)
MOD = 10 ** 9 + 7

for k, v in c.items():
    if v != 2:
        if N % 2 == 1 and k == 0:
            continue
        else:
            print("0")
            break
else:
    print(2 ** (N // 2) % MOD)
