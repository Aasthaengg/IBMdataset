S=input()
T=input()
num=0
for i in range(len(S)):
    if S[i]==T[i]:
        num+=1
    else:
        print("No")
        exit()
if num==len(S):
    print("Yes")
