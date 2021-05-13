S=input()
N=len(S)

A="keyence"
F=(S==A)
for i in range(N):
    for j in range(i+1,N+1):
        F|=(S[:i]+S[j:]==A)

if F:
    print("YES")
else:
    print("NO")
