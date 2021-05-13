# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
exp = [0] * (N+1)
for i in range(2, N+1):
    cur = i
    for p in range(2, i+1):
        while cur % p == 0:
            exp[p] += 1
            cur //= p

def num(x):
    '''冪乗がx-1以上の数を返す'''
    return len(list(filter(lambda y: y >= x-1, exp)))

answer = num(75) + num(25) * (num(3)-1) + num(15) * (num(5)-1)\
        + num(5) * (num(5)-1) * (num(3)-2) // 2
print(answer)
