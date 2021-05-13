import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    cnt=1
    for i in l:
        if i%2==1:
            cnt*=1
        else:
            cnt*=2
    print(3**n-cnt)
resolve()
