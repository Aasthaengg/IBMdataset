N=int(input())
S=input()
x=0
X=[0]
for i in S:
    if i=="I":
        x+=1
        X.append(x)
    else:
        x-=1
        X.append(x)
print(max(X))