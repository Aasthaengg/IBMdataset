import sys
input=sys.stdin.readline
n,a,b = map(int, input().split())
h=[int(input()) for i in range(n)]

def solve(num):
    all_b = num*b
    cnt=0
    for i in range(len(h)):
        rest = h[i] - all_b
        if rest>0:
            cnt+=(rest - 1) // (a-b) + 1
    if cnt <= num:
        return True
    else:
        return False

l=0
r=10**20
while r-l>1:
    mid=(l+r)//2

    if solve(mid):
        r=mid
    else:
        l=mid
print(r)