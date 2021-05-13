# inp.readline()
# int(inp.readline())
# out.write()
# raw_input()
# map(int,raw_input().split())
# map(int,inp.readline().split())
# for _ in xrange(input()):
# print "Case #"+str(_+1)+": "+ 
if __name__ == "__main__":
    from sys import stdin as inp, stdout as out,setrecursionlimit as srl
    from collections import Counter,defaultdict,deque
    from heapq import *
    def upd(idx,v):
      while idx<len(b):
        b[idx]=(b[idx]+v)%mod
        idx+=(idx&-idx)
    def acc(idx):
        s=0
        while idx>0:
            s=(s+b[idx])%mod
            idx-=(idx&-idx)
        return s
    for _ in xrange(1):
        n,k=map(int,inp.readline().split())
        a=[map(int,inp.readline().split()) for i in xrange(k)]
        b=[0]*(n+1)
        mod=998244353
        upd(1,1)
        for i in xrange(2,n+1):
          for l,r in a:
            upd(i,acc(max(0,i-l))-acc(max(0,i-r-1))%mod)
        print (acc(n)-acc(n-1))%mod