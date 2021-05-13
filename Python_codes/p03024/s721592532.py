import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    s=str(input())
    l=len(s)
    val=s.count('o')
    if val+15-l>=8:
        print('YES')
    else: print('NO')
    
resolve()