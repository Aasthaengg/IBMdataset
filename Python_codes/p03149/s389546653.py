# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    l=list(map(int,input().split()))
    if l.count(1) and l.count(9) and l.count(7) and l.count(4):
        print('YES')
    else:
        print('NO')
    
resolve()