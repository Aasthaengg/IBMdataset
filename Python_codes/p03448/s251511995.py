import sys
A,B,C,X=map(int,sys.stdin)

ans=0
for i in range(A+1):
    for j in range(B+1):
        if 0<=X-(i*500+j*100)<=C*50:
            ans+=1

print(ans)
