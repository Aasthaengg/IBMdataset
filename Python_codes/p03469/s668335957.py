import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    s=str(input())
    print('2018'+s[4:])

    
resolve()