S=input()
T=input()
l=len(S)
j=0
for i in range(l): 
    if S[i]!=T[i]:
        j=j+1
print(j)