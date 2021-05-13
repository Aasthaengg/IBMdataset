import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    if sum(l)%2==1:
        print('NO')
    else:
        print('YES')
resolve()
