import sys
import math

#https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

 #ランレングス圧縮
def rle_comp(S):
     rle = []
     chain = 0
     for c in S:
         if c == 'x':
             chain += 1
         else:
            rle.append(chain)
            chain = 0
     rle.append(chain)
 
     #print(rle)
     return rle

s = input()
ans = 0

#xを除外した文字列の生成,回文判定
t = [i for i in s if i != 'x']
t2 = t[::-1]
if t != t2:
    ans = -1

#xを挿入する回数の計算
if ans != -1:
    N = len(t)
    #ランレングス圧縮して 'x' の個数ベクトルを求める
    nums = rle_comp(s)

    for i in range(len(nums)//2):
        #左端と右端の要素をを内側に向けて１つずつ比較していく
        ans += max(nums[i], nums[ len(nums)-1-i]) - min(nums[i], nums[ len(nums)-1-i])

print(ans)

