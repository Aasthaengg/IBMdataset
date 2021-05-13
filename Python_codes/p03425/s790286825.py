N=int(input())
M=[]
A=[]
R=[]
C=[]
H=[]

for i in range(N):
    tmp=input()
    if tmp[0]=="M":
        M.append(tmp)
    elif tmp[0]=="A":
        A.append(tmp)
    elif tmp[0]=="R":
        R.append(tmp)
    elif tmp[0]=="C":
        C.append(tmp)
    elif tmp[0]=="H":
        H.append(tmp)

m=len(M)
a=len(A)
r=len(R)
c=len(C)
h=len(H)

if len(M)+len(A)+len(R)+len(C)+len(H)<=2:
    print(0)
else:
    print(m*a*r+m*a*c+m*a*h+m*r*c+m*r*h+m*c*h+a*r*c+a*c*h+ a*r*h+r*c*h)