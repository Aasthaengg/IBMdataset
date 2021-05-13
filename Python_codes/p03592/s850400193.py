N,M,K=map(int,input().split())
F=False

for x in range(N+1):
    for y in range(M+1):
        F|=(x*(M-y)+y*(N-x)==K)

if F:
    print("Yes")
else:
    print("No")
