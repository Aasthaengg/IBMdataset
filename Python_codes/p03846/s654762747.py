from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)
MOD = 10**9 + 7

# print('c', c)
if N % 2 == 0:
    for key, value in c.items():
        if key % 2 != 1:
            print(0)
            exit()
        if value != 2:
            print(0)
            exit()
else:
    if c.get(0) is None:
        print(0)
        exit()
    for key, value in c.items():
        if key == 0:
            continue
        if key % 2 != 0:
            print(0)
            exit()
        if value != 2:
            print(0)
            exit()
ans = pow(2, N // 2, MOD)
print(ans)
