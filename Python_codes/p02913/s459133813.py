#ABC141-E Who Says a Pun?
"""
最長共通部分文字列を求める問題。
最長共通接頭辞(z-algorithm)を用いて、O(N**2)で求まる。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

def Z_algorithm(s):
    N = len(s)
    Z_alg = [0]*N
    Z_alg[0] = N
    i = 1
    j = 0
    res = 0 #文字列非重複の場合の最大共通部分
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        if i+1 > j:
            res = max(res,j)
        else:
            res = max(res,i)
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_alg[k]<j:
            Z_alg[i+k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return res
n = int(readline())
s = readline().rstrip().decode('utf-8')
ans = 0
i = 0
while True:
    ans = max(ans,Z_algorithm(s))
    if len(s)<=2:
        break
    s = s[1:]
    i += 1

print(ans)