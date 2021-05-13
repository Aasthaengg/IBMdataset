### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest

def resolve():
    readline=sys.stdin.readline
    mod=10**9+7
    n=int(readline())
    arr=list(map(int, readline().rstrip().split()))
    binArr = [[0 for i in range(60)] for j in range(n)]
    cnt=[0]*60
    for i in range(n):
        b = bin(arr[i])[2:]
        lenb = len(b)
        for j in range(lenb):
            binArr[i][j] = int(b[lenb-1-j])
            cnt[j]+=binArr[i][j]
    ans=[0]*60
    answer = 0
    for i in range(n):
        for j in range(60):
            # 1: cnt[j]
            # 0: n-cnt[j]
            cnt[j]-=binArr[i][j]
            if binArr[i][j] == 0:
                ans[j] += cnt[j]
            else:
                ans[j] += (n-cnt[j]-i-1)
    x=1
    for i in range(60):
        answer += ans[i]*x
        answer %= mod
        x*=2
        x%=mod
    print(answer)
    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------