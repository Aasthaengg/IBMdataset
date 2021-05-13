import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=[list(input().split()) for i in range(n)]
    x=input()
    cnt=0
    flag=False
    for s,t in l:
        if s==x:
            flag=True
        if s!=x and flag:
            cnt+=int(t)
    print(cnt)
resolve()