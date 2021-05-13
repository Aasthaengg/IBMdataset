s=int(input())
A=[s]
while s!=1:
    if s%2==0:
        s=s//2
        A.append(s)
    else:
        s=(3*s)+1
        A.append(s)
AA=A+[4,2,1]
if AA[0]==1 or AA[0]==2:
    print(4)
else:
    for m in range(len(AA)):
        for n in range(len(AA)):
            if AA[m]==AA[n] and m>n:
                M=m-1
                break
    print(M)