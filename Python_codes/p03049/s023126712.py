N=int(input())
S=[""]*N
for i in range(N):
    S[i]=input()

H=0
A,B,C=0,0,0
for s in S:
    for j in range(len(s)-1):
        if s[j:j+2]=="AB":
            H+=1

    if s[0]=="B" and s[-1]=="A":
        C+=1
    elif s[0]=="B":
        B+=1
    elif s[-1]=="A":
        A+=1

if C==0:
    D=min(A,B)
else:
    if A+B!=0:
        D=C+min(A,B)
    else:
        D=C-1
        
print(H+D)
