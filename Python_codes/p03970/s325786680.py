S=list(input())
Scor=list("CODEFESTIVAL2016")
#print(S,Scor)
c=0
for i in range(len(S)):
    if not(S[i]==Scor[i]):
        c=c+1
print(c)