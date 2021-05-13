X,Y=map(int,input().split())
def pr(n,prize):
    c=0
    if n==1:
        c=c+300000
    elif n==2:
        c=c+200000
    elif n==3:
        c=c+100000
    return prize+c
prize=0
prize=pr(X,prize)
prize=pr(Y,prize)
if (X==1)and(Y==1):
    prize=prize+400000
print(prize)