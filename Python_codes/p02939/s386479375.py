S=input()
T=""
U=""
K=0
for s in S:
    U+=s
    if T!=U:
        K+=1
        T=U
        U=""

print(K)
