
import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    ans=10**9
    l=[list(map(int,input().split())) for i in range(n)]
    l.sort(key=lambda x:x[0])
    print(l[-1][0]+l[-1][1])
resolve()