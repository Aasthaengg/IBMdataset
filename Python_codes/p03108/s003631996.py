import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd
class UnionFind(): #集合の取り扱い、辺に重み、階層を意識するときは使えない
    def __init__(self,n):
        self.n=n
        self.par = [-1]*n
    def find(self,x):
        if self.par[x] <0: #負なら親、要素数
            return x
        else: #正なら親の番号
            self.par[x]=self.find(self.par[x]) #一回調べたら根を繋ぎ変える、経路圧縮
            return self.par[x]
    def union(self,x,y):
        x=self.find(x) #x,yの親
        y=self.find(y)

        if x==y: #親が同じなら何もしない
            return 
        if self.par[x]>self.par[y]: #要素数が大きい方をxにする
            x,y=y,x
        self.par[x]+=self.par[y] #xがある集合にyが入った集合をくっつける
        self.par[y]=x

    def size(self,x):
        return -self.par[self.find(x)] #親のサイズ
    
    def same(self,x,y): #親が同じ、すなわち同じ集合か
        return self.find(x)==self.find(y)

    def member(self,x): #同じ木（集合）にある要素全部リストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i)==root ]
    
    def roots(self): #集合の根になってる要素をリストで返す
        return [i for i , x in enumerate(self.par) if x<0]
    
    def group_count(self): #集合の数、木の数
        return len(self.roots())

    def all_member(self): #辞書型で返す
        return {r: self.member(r) for r in self.roots()}
    def __str__(self):
        return "\n".join('{}:{}'.format(r,self.member(r)) for r in self.roots)


input=sys.stdin.readline
n,m=map(int,input().split())
v=tuple(tuple(map(lambda x: int(x)-1,input().split())) for _ in range(m))
ans=[0]*m
ans[-1]=(n*(n-1))//2

tree=UnionFind(n)
for i in range(1,m):
    a,b=v[m-i]
    if tree.same(a,b):
        ans[m-i-1]=ans[m-i]
        continue
    n1=tree.size(a)
    n2=tree.size(b)
    tree.union(a,b)
    ans[m-i-1]=ans[m-i]-(n1*n2)
print(*ans)