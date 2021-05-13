import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c=map(int, input().split())
    if a%2==0 or b%2==0 or c%2==0:
        print(0)
    else:
        l=[a,b,c]
        l.sort()
        print(l[0]*l[1])
resolve()
