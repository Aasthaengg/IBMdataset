import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
s = S()

l = []

for i in range(len(s) - 2):
  l.append(int(s[i:i+3]))

sa = [abs(753 - i) for i in l]
print(min(sa))