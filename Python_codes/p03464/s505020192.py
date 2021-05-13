import sys
K=int(input())
A=[int(i) for i in input().split()]
B=A[::-1]
if B[0]!=2:
    print(-1)
    sys.exit()
a=2
b=3
for i in range(1,K):
    x=B[i]
    if a%x==0:
        c=a
    else:
        c=((a//x)+1)*x
    if a<=c<=b:
        a=c
        b=((b//x)+1)*x-1

    else:
        print(-1)
        sys.exit()
    #print(a,b,c,x)
print(a,b)