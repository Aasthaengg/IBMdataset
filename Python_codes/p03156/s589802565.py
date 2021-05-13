import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    a,b=map(int, input().split())
    l=list(map(int,input().split()))
    cnt1=0
    cnt2=0
    cnt3=0

    for i in l:
        if i<=a:
            cnt1+=1
        elif a+1<=i<=b:
            cnt2+=1
        else:
            cnt3+=1
    print(min(cnt1,cnt2,cnt3))


resolve()