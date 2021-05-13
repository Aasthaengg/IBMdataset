S=input()
z=0
o=0
for i in range(len(S)):
    if S[i]=="0":
        z+=1
    elif S[i]=="1":
        o+=1
print(2*min(z,o))