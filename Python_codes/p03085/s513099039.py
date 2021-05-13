import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
b = S()
ans = ''
if b == 'A':
    ans = 'T'
if b == 'C':
    ans = 'G'
if b == 'G':
    ans = 'C'
if b == 'T':
    ans = 'A'
print(ans)