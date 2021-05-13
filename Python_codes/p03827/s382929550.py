N=int(input())
S=list(input())
x=0
X=[0]
for i in range(N):
    if S[i]=='I':
        x+=1
        X.append(x)
    elif S[i]=='D':
        x-=1
        X.append(x)
print(max(X))