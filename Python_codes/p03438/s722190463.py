import sys
input = sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

cnt =0
for ai,bi in zip(a,b):
    if ai<=bi:
        cnt+= (bi-ai)//2
    else:
        cnt+= bi-ai

if cnt>=0:
    print('Yes')
else:
    print('No')
