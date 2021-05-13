import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    l1=list(input())
    l2=list(input())
    l3=list(input())
    print(l1[0]+l2[1]+l3[2])
resolve()