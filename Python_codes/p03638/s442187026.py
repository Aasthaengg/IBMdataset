import sys
input = sys.stdin.readline
H,W=map(int,input().split())
n=int(input())
ans=[[0]*W for _ in range(H)]

A=list(map(int,input().split()))
cnt=0
for a,num in enumerate(A):
    #print(a,num)
    for i in range(num):
        h=cnt//W
        w=cnt %W
        if h%2==1:
            w=w*(-1)-1
        ans[h][w]=a+1
        cnt+=1
for a in ans:
    print(*a)
