# coding: utf-8
# Your code here!
# coding: utf-8
from fractions import gcd 
from functools import reduce
import sys
sys.setrecursionlimit(200000000)
from inspect import currentframe


# my functions here!
#標準エラー出力
def printargs2err(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' : '+repr(arg) for arg in args),file=sys.stderr)
def debug(x):
    print(x,file=sys.stderr)
def printglobals():
    for (symbol, value) in globals().items():
        print('symbol="%s"、value=%s' % (symbol, value),file=sys.stderr)
def printlocals():
    for (symbol, value) in locals().items():
        print('symbol="%s"、value=%s' % (symbol, value),file=sys.stderr)
#入力（後でいじる）
def pin(type=int):
    return map(type,input().split())
#どっかで最悪計算量の入力データを用意する関数を作ろう？
def worstdata():
    a=0
    return a
#solution:
def vacation(N,act):
    lastact =[]
    dp=[0,max(act[0])]*(N+1) #[i]日目のActivity で得られる最大幸福量
    
    return 0

#input


N,T=pin()
timing=tuple(pin())

ans=0
for i in range(N):
        if i!=(N-1):ans+=min(timing[i+1]-timing[i],T)
        else:ans+=T
print(ans)
#output
#print(solution(H,N))
#print(["No","Yes"][cond])

