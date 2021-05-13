S=input()
F=0
for i in range(len(S)):
    if F==0:
        if S[i]=="C":
            F=1
    if F==1:
        if S[i]=="F":
            print("Yes")
            exit()
print("No")