import math
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

A=10*(math.ceil(a/10))
B=10*(math.ceil(b/10))
C=10*(math.ceil(c/10))
D=10*(math.ceil(d/10))
E=10*(math.ceil(e/10))

re1=A-a
re2=B-b
re3=C-c
re4=D-d
re5=E-e
result=[[re1,A],[re2,B],[re3,C],[re4,D],[re5,E]]
result.sort()
ans=0
for i in range(5):
    if i==4:
        ans+=result[i][1]-result[i][0]
        break
    ans+=result[i][1]
print(ans)