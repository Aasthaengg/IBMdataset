import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
import math
from copy import copy, deepcopy
from copy import deepcopy as dcp
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque, defaultdict
#deque(l), pop(), append(x), popleft(), appendleft(x)
#q.rotate(n)で → にn回ローテート
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate,combinations,permutations#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
#import fractions#古いatcoderコンテストの場合GCDなどはここからimportする
from functools import reduce,lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率
from decimal import Decimal

def input(): 
    x=sys.stdin.readline()
    return x[:-1] if x[-1]=="\n" else x
def printe(*x):print("## ",*x,file=sys.stderr)
def printl(li): _=print(*li, sep="\n") if li else None
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds
def alp2num(c,cap=False): return ord(c)-97 if not cap else ord(c)-65
def num2alp(i,cap=False): return chr(i+97) if not cap else chr(i+65)
def matmat(A,B):
    K,N,M=len(B),len(A),len(B[0])
    return [[sum([(A[i][k]*B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]
def matvec(M,v):
    N,size=len(v),len(M)
    return [sum([M[i][j]*v[j] for j in range(N)]) for i in range(size)]
def T(M):
    n,m=len(M),len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]
def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reverse=True)  #二個目の要素で降順並び替え

    #N = int(input())
    H, W = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    S = tuple(tuple(input()) for i in range(H)) #改行行列

    cnt=[[[0]*W for _ in range(H)] for _ in range(4)]
    for i in range(0,H):
        mj=-1
        for j in range(0,W):
            if S[i][j]=="#":
                mj=j
                continue
            cnt[0][i][j]=(j-mj-1)
    for i in range(0,H):
        mj=W
        for j in range(W-1,-1,-1):
            if S[i][j]=="#":
                mj=j
                continue
            cnt[1][i][j]=(mj-j-1)

    for i in range(0,W):
        mj=-1
        for j in range(0,H):
            if S[j][i]=="#":
                mj=j
                continue
            #printe(j,i)
            cnt[2][j][i]=(j-mj-1)
    for i in range(0,W):
        mj=H
        for j in range(H-1,-1,-1):
            if S[j][i]=="#":
                mj=j
                continue
            cnt[3][j][i]=(mj-j-1)
    
    ans=0
    for i in range(0,H):
        for j in range(0,W):
            if S[i][j]=="#":
                continue
            x=cnt[0][i][j]+cnt[1][i][j]+cnt[2][i][j]+cnt[3][i][j]+1    
            ans=max(x,ans)
    print(ans)



if __name__ == "__main__":
    main()