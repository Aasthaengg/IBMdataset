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
        a=map(lambda x:x[0]==x[1],[map(int,inp.readline().split()) for i in  xrange(n)])
        print 'Yes' if any(all(a[i:i+3]) for i in xrange(n-2)) else 'No'