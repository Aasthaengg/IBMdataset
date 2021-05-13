A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
a=A%10
b=B%10
c=C%10
d=D%10
e=E%10
result=0
if a==0:
    result+=A
else:
    result+=(A+10-a)
if b==0:
    result+=B
else:
    result+=(B+10-b)
if c==0:
    result+=C
else:
    result+=(C+10-c)
if d==0:
    result+=D
else:
    result+=(D+10-d)
if e==0:
    result+=E
else:
    result+=(E+10-e)
if a==b==c==d==e==0:
    print(result)
else:
    l=set([a,b,c,d,e])
    l.discard(0)
    print(result-(10-min(l)))
