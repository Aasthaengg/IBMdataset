import collections
n = int(input())
dat = list(map(int, input().split()))
dat.sort()
f = True
if n % 2 == 0: # 偶数
    for i in range(n):
        if dat[i] != 2 * (i // 2) + 1:
            f = False
    if f:
        print(2 ** (n // 2) % (1000000000+7) )
else: # 奇数
    if dat[0] != 0:
        f = False
    for i in range(n - 1):
        if dat[i + 1] != 2 * (i//2 + 1):
            f = False
    if f:
        print(2** (n //2 ) % (1000000000+7) )
if f is False:
    print(0)
