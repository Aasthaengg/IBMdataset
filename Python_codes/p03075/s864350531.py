import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
li = [I() for _ in range(6)] #n行に１つずつ入力される整数
if (li[4] - li[0]) <= li[5]:
    print('Yay!')
else:
    print(':(')