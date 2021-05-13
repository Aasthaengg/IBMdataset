A=list(input())
N=len(A)

S=N*(N-1)//2+1

for s in "abcdefghijklmnopqrstuvwxyz":
    n=A.count(s)
    if n>=2:
        S=S-n*(n-1)//2

print(S)