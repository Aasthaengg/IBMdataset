n, k = map(int, input().split())
an = list(map(int, input().split()))
for i in range(n):
    an[i] -= 1
    
import math
dv = []
dv.append(an)
K = k
N = n
for _ in range(1, int(math.log2(K)) + 1):
    l = [0] * N
    dv.append(l)

for k in range(1, int(math.log2(K)) + 1):
    for n in range(N):
        dv[k][n] = dv[k - 1][dv[k - 1][n]]
        
# N 回目を 2 ^ t で表すためにビット演算を用いる
# a : dv の何行目を用いるかを格納
a = []
for i in range(int(math.log2(K)) + 1):
    if K >> i & 1:
        a.append(i)
        
now = 0
for i in a:
    now = dv[i][now]
        
print(now + 1)