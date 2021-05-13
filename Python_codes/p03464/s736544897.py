#AGC020-B Ice Rink Game
"""
逆操作を考える。
何人組を作るということは、modにおける最大値と最小値を求め続けるということ。
そのような組が作れないような場合(全員が脱落するような場合)は、-1を出力。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

k = int(readline())
lst1 = list(map(int,readline().split()))
lst1.reverse()
if lst1[0] != 2:
    print(-1)
    exit()


def min_lot(value,unit):
    if value%unit == 0:
        return value//unit
    else:
        return value//unit + 1
mn = 2
mx = 3
for i in range(1,k):
    res = min_lot(mn,lst1[i])

    if not mn <= res*lst1[i] <= mx:
        print(-1)
        exit()

    mn = res*lst1[i]

    lim = (mx//lst1[i] + 1)*lst1[i] - 1
    mx = lim



print(mn,mx)