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
        n=input()
        t=int(pow(n,0.5))+1
        c=Counter()
        for i in xrange(1,t+1):
          for j in xrange(i*i,n+1,i):
            c[j]+=1
        print 2*sum(c[i] for i in xrange(1,n))-int(pow(n-1,0.5))