import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    l=list(input().split())
    l.sort(reverse=True)
    print(int(l[0]+l[1])+int(l[2]))
resolve()