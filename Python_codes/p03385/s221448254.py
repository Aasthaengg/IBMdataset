S=str(input())
X="abc"
Y=[]
for i in range(3):       
    if S[i] in X:
        if S[i] not in Y:
            Y.append(S[i])
if len(Y)==3:
    ans="Yes"
else:
    ans="No"
print(ans)