import sys
"""
方針：まず左端を固定して実際にPで割ったあまりを計算しながら数値列を伸ばしていけばO(N^2)で計算ができる
文字列の左右を固定した場合に（部分文字列について？）Pで割ったあまりを計算できないか，定式化を考えてみよう．
Ui := S[i:N]をSのi文字以降を評価した整数と置く．便宜上UN+1=0とする．
この時Sのi文字目からj文字目までを評価した整数は(Ui - Uj+1)/10^(j+1-i)と表せる．

"""

sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline
read = sys.stdin.read

n, p = [int(i) for i in readline().split()]
s = input()

if p == 2 or p == 5:
    ans = 0
    for i, c in enumerate(s):
        if int(c) % p == 0:
            ans += i + 1
    print(ans)
    exit()


res = [0] * p
res[0] = 1
t = 1
now = 0
for i in s[::-1]:
    i = int(i)
    now += i * t
    now %= p
    res[now] += 1
    t = t * 10 % p
    


ans = 0
for i in res:
    ans += i * (i - 1) // 2

print(ans)

