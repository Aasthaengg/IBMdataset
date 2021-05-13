N=int(input())
S=sorted([int(input()) for i in range(N)])
s=sum(S)
if s%10==0:
    for a in S:
        if a%10!=0:
            s-=a
            break
    else:
        s=0
print(s)