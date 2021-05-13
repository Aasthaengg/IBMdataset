n=int(input())
s=sorted([int(input()) for i in range(n)])
S=sum(s)
if S%10!=0:
    print(S)
else:
    flag=False
    for i in s:
        tmp=S-i
        if tmp%10!=0:
            flag=True
            break
    print(tmp if flag else 0)