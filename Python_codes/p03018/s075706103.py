S = input()
N = len(S)
X = []
x = 0
while x<N-1:
    if S[x]=="B" and S[x+1]=="C":
        X.append("D")
        x+=1
    else:
        X.append(S[x])
    x+=1
ans = 0
N = len(X)
a = 0
for i in range(N):
    if X[i]=="A":
        a+=1
    elif X[i]=="D":
        ans+=a
    else:
        a=0
print(ans)