N,A,B,C,D=map(int,input().split())

S=input()
jump=False
n=0
R=0

for i in range(A-1,D):
    if S[i]=="#":
        R+=1
        n=0
        if R>=2:
            print("No")
            exit()
    else:
        n+=1
        R=0

b=0
S=S+"G"
for j in range(B-2,D+1):
    if S[j]==".":
        b+=1
        if b>=3:
            print("Yes")
            exit()
    else:
        b=0

if C<D:
    print("Yes")
else:
    print("No")
    
