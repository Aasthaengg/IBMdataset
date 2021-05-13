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

# 階乗の事前計算
x = [1]
res = 1
for i in range(1, N + 1):
    res *= i
    x.append(res)

def cmb(n, r):
    return x[n] // (x[r] * x[n - r])

ans = 0 # 偶数になる場合の数

for k in range(kisu + 1):
    if k % 2 == 0:
        # 奇数が偶数個（0個含む） + 偶数が0個以上
        ans += cmb(kisu, k) * (2 ** gusu)

if P == 0:
    print(ans)
else:
    print(total - ans)