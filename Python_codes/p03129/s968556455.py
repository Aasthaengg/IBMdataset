import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,k=map(int, input().split())
    num=-(-n // 2)
    if num<k:
        print('NO')
    else:
        print('YES')
resolve()