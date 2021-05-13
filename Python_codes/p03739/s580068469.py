from itertools import accumulate

n=int(input())
a=list(map(int,input().split()))

s=list(accumulate(a))

chg=0
sign=1
op1=0

for i in range(n):
    curs=s[i]+chg

    if sign*curs>0:
        sign*=-1
        continue

    chg+=sign-curs
    a[i]+=sign-curs
    op1+=abs(sign-curs)

    sign*=-1

chg=0
sign=-1
op2=0

for i in range(n):
    curs=s[i]+chg

    if sign*curs>0:
        sign*=-1
        continue

    chg+=sign-curs
    a[i]+=sign-curs
    op2+=abs(sign-curs)

    sign*=-1

print(min(op1,op2))