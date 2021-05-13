from sys import exit
from math import gcd

def segfunc(x, y):
    '''
    問題に応じて返り値を設定
    '''
    return gcd(x, y)


def init(a):
    '''
    配列aで初期化
    '''
    for i in range(n):
        seg[i+num-1] = a[i]    
    for i in range(num-2, -1, -1) :
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2])


def query(p, q):
    '''
    [p, q)についてsegfuncを適用したものを返す
    '''
    if q <= p:
        return ide_ele
    
    p += num - 1
    q += num - 2
    res = ide_ele

    while q - p > 1:
        if p & 1 == 0:
            res = segfunc(res, seg[p])
        if q & 1 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p // 2
        q = (q - 1) // 2
    
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(res, segfunc(seg[p], seg[q]))
    
    return res


n, k = map(int, input().split())
a = list(map(int, input().split()))

if k > max(a):
    print('IMPOSSIBLE')
    exit()

num = (2 ** len(bin(n - 1)) - 2)
ide_ele = 0
seg = [ide_ele] * 2 * num

init(a)

if k % query(0, n) == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')