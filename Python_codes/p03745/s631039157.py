import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    prev='ryouhou'
    cnt=0
    for i in range(n-1):
        if l[i+1]-l[i]>0:
            if prev=='-':
                cnt+=1
                prev='ryouhou'
            else:
                prev='+'
        elif l[i+1]-l[i]<0:
            if prev=='+':
                cnt+=1
                prev='ryouhou'
            else:
                prev='-'
    print(cnt+1)
resolve()