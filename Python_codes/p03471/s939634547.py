import sys
n,y=map(int,input().split())
for i in range(n+1):
    for j in range(n+1-i):
        cul=10000*i+5000*j
        if cul>y:
            break
        if cul+1000*(n-i-j)==y:
            print(i,j,n-i-j)
            sys.exit()
print(-1,-1,-1)