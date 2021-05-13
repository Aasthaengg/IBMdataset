#ABC175-D
"""
1周未満で終わる時の最大値をまずもとめる
(i)k<一周なら
最大値を出力して終了
(ii)sum(lst) <= 0
1周以上する価値はないので、最大値を出力して終了
(iii)sum(lst) > 0
N%kの端数だけ愚直にもう一度最大値を求めて出力
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,k = map(int,readline().split())
p = list(map(int,readline().split()))
c = list(map(int,readline().split()))
p = [i-1 for i in p]

ans = -10**18

for i in range(n):
    lst1 = [c[i]]
    idx = p[i]
    while idx != i:
        lst1.append(c[idx])
        idx = p[idx]
    sm = sum(lst1)
    acc = 0
    for i in range(min(len(lst1),k+2)):
        acc += lst1[i]
        a = acc
        if sm > 0:
            a += sm*((k-(i+1))//len(lst1))
        ans = max(a,ans)
print(ans)
