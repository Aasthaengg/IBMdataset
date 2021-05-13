N,A,B,C,D=map(int,input().split())
S=input()
a=1
for i in range(A,C-2):
    if S[i]==S[i+1]=="#":
        a=0
        break
for i in range(B,D-2):
    if S[i]==S[i+1]=="#":
        a=0
        break
if C>D:
    for i in range(B-1,D):
        if S[i-1]==S[i]==S[i+1]==".":
            break
    else:
        a=0
print("Yes" if a else "No")