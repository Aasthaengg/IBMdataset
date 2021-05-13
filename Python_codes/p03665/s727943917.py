import sys
N, P = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

kisu = 0
gusu = 0
for a in A:
    if a % 2 == 1:
        kisu += 1
    else:
        gusu += 1

total = 2 ** N # 全場合の数
if kisu == 0:
    ans = 2 ** gusu
else:   
    ans = (2 ** gusu) * (2 ** (kisu - 1)) # 偶数になる場合の数

if P == 0:
    print(ans)
else:
    print(total - ans)