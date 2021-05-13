import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=[0]+list(map(int,input().split()))
    cnt=0
    for i in range(1,n+1):
        if l[l[i]]==i:
            cnt+=1
    print(cnt//2)
resolve()