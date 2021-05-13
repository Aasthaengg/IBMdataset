S=input()

U=0
A=""
B=""
for i in range(len(S)):
    A+=S[i]
    if A==B:
        continue
    B=A
    A=""
    U+=1
print(U)
