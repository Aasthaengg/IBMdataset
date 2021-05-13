S=input()
l=len(S)
L=[]
for i in range(l-2):
    L.append(abs(753-int(S[i:i+3])))
print(min(L))