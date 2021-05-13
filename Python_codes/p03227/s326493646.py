import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    s=str(input())
    print(s if len(s)==2 else s[::-1])

resolve()