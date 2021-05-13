N,K=map(int,input().split())
S=input()
S="*"+S+"*"

A=0
for i in range(1,N+1):
    if S[i]=="L":
        A+=(S[i-1]=="L")
    elif S[i]=="R":
        A+=(S[i+1]=="R")

for i in range(K):
    A=min(N-1,A+2)

print(A)
