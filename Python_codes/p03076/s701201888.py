import math
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
A=math.ceil(A/10)*10
B=math.ceil(B/10)*10
C=math.ceil(C/10)*10
D=math.ceil(D/10)*10
E=math.ceil(E/10)*10
abcde=[a,b,c,d,e]
small=min(abcde)
abcde.sort()
while (small==0) & (len(abcde)!=0):
    try:
        del abcde[0]
        small=abcde[0]
    except:
        pass
if len(abcde)==0:
    small=10
print(A+B+C+D+E-(10-small))