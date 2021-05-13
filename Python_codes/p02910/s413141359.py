S=input()
count=0
Ans=True
for i in range(len(S)):
    if i%2==1 and S[i]=="R":
        Ans=False
    elif i%2==0 and S[i]=="L": 
        Ans=False
if Ans==True:
    print("Yes")
else:
    print("No")