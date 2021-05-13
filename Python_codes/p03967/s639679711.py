S=input()

K=0
for i in range(len(S)):
    if i%2==0 and S[i]=="p":
        K-=1
    elif i%2==1 and S[i]=="g":
        K+=1
print(K)