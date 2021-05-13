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
    for _ in xrange(1):
        n,k=map(int,inp.readline().split())
        a=[map(int,inp.readline().split()) for i in xrange(k)]
        b=[0]*(n+1)
        b[1]=1
        mod=998244353
        for i in xrange(2,n+1):
          b[i]=b[i-1]
          for l,r in a:
            b[i]=(b[i]+b[max(0,i-l)]-b[max(0,i-r-1)])%mod
        print (b[-1]-b[-2])%mod