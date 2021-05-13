#第一回日本最強プログラマー学生選手権-予選- -B Kleene Inversion
"""
リストをk回繰り返したものの、転倒数の個数を求めよ
先ず純粋に与えられたリスト内での転倒数を求めた後、
それを1~k倍したものを足し合わせる
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
mod = 10**9+7

n,k = map(int,readline().split())
lst1 = list(map(int,readline().split()))
fall = 0
fall_al = 0
for i in range(n-1):
    for j in range(i+1,n):
        if lst1[i] > lst1[j]:
            fall += 1
lst1.sort(reverse=True)
for i in range(n-1):
    for j in range(i+1,n):
        if lst1[i] > lst1[j]:
            fall_al += 1

def reydeoro(n):
    return n*(n+1)//2
print((fall*k+fall_al*reydeoro(k-1))%mod)