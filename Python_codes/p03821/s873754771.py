import sys
from fractions import gcd
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
ans = 0
a = []
b = []
for i in range(n):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)

a = a[::-1]
b = b[::-1]

for i in range(n):
    if (ans + a[i]) % b[i] == 0:
        pass
    else:
        ans += b[i] - ((ans + a[i]) % b[i])

    # #bの方が大きい
    # if a[i] < b[i]:
    #     ans += b[i] - ((ans + a[i]) % b[i])
    # # aと増加分の方が大きい
    # else:
    #     # ボタン押さなくて良い場合
    #     if (ans + a[i]) % b[i] == 0:
    #         continue
    #     else:
    #         ans += b[i] - ((ans + a[i]) % b[i])

print(ans)
