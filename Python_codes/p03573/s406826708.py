import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    l=list(map(int,input().split()))
    for i in l:
        if l.count(i)==1:
            print(i)
            break
resolve()