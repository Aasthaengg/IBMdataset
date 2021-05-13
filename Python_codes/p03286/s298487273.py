n=int(input())
now=1
A=[]
while n!=0:
    if n%(now*2)==0:
        A.append(0)
    else:
        A.append(1)
        n-=now
    now*=-2
A=list(reversed(A))
S=""
for a in A:
    S+=str(a)
if len(S)==0:
    print(0)
else:
    print(S)