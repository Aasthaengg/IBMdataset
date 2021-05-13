import sys
input=sys.stdin.readline
n=int(input())

def bin(start):
    ok=0
    ng=n
    while abs(ng-ok)>1:
        mid=(ok+ng)//2
        print(mid)
        sys.stdout.flush()
        s=input()
        if s=='Vacant':exit()
        if mid%2==0 and start==s:
            ok=mid
        elif mid%2!=0 and start!=s:
            ok=mid
        else:
            ng=mid
print(0)
sys.stdout.flush()
start=input()
if start=='Vacant':exit()
bin(start)
