import math
#切る回数を足してK以下ならOK
def ok(l):
    x =sum([math.ceil(a/l) -1 for a in A])
    if x <=K:
        return True
   # else:
    #    return False

# 初期入力
import bisect
import sys
input = sys.stdin.readline  #文字列では使わない
N,K = map(int, input().split())
A = list(map(int, input().split()))

#2分探索
bottom,top =0,max(A)
while top -bottom >1:
    mid =(top +bottom)//2
    if ok(mid):
        top =mid
    else:
        bottom =mid
print(top)