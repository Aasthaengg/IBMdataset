
import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    check=[0]*8
    tuyo=0
    for i in l:
        x=i//400
        if x>=8:
            tuyo+=1
        else:
            check[x]+=1
    if tuyo==n:
        print(1,tuyo)
    else:
        cnt=0
        for j in check:
            if j>0:
                cnt+=1
        print(cnt,cnt+tuyo)
resolve()