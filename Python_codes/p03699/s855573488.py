import sys
n=int(input())
l=sorted([int(input()) for _ in range(n)])
sm=sum(l)

if sm%10!=0:
    print(sm)
    sys.exit()
    
else:
    for i in range(n):
        if l[i]%10!=0:
            print(sm-l[i])
            sys.exit()
print(0)
