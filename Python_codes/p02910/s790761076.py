S = input()
N=len(S)
x="Yes"
for i in range(0,N):
    if i%2==0 and S[i]=="L":
        x="No"
        break
    elif i%2==1 and S[i]=="R":
        x="No"
        break
print(x)