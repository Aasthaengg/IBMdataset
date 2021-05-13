N, A, B, C, D = map(int, input().split())
N-=1
A-=1
B-=1
C-=1
D-=1
S = input()

overtakeFlag = False 
proceedableFlag = True
if C > D:
    for i in range(B, D+1):
        if S[i-1] == "." and S[i] == "." and S[i+1] == ".":
            overtakeFlag = True
else:
    overtakeFlag = True

for i in range(A, max(C, D)-1):
    if S[i]=="#" and S[i+1]=="#":
        proceedableFlag = False

if overtakeFlag and proceedableFlag:
    print("Yes")
else:
    print("No")
