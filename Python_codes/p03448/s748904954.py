import sys
A,B,C,X=map(int,sys.stdin)

ans=0
for i in range(min(A,X//500)+1):
    ta=X-i*500
    for j in range(min(B,ta//100)+1):
        tb=ta-j*100
        if C*50>=tb:
            ans+=1

print(ans)
