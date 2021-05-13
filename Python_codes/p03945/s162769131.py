S=input()

X=0
for i in range(1,len(S)):
    if S[i]!=S[i-1]:
        X+=1
print(X)
