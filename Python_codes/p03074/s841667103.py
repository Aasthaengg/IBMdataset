n,k = map(int, input().split())
*s, =map(int, input())
mark=[]
for i in range(n):
    if i==0 and s[i]==1:
        mark.append((i,1))
    elif i==0 and s[i]==0:
        mark.append((i,0))
    elif s[i-1]==0 and s[i]==1:
        mark.append((i,1))
    elif s[i-1]==1 and s[i]==0:
        mark.append((i,0))

X=[0]*n
for i in range(len(mark)):
    ist,jst=mark[i]
    if jst==0:
        if i+2*k<len(mark):
            igo, jgo=mark[i+2*k]
            X[ist]=igo-ist
        else:
            X[ist]=n-ist
    if jst==1:
        if i+2*k+1<len(mark):
            igo, jgo=mark[i+2*k+1]
            X[ist]=igo-ist
        else:
            X[ist]=n-ist

print(max(X))