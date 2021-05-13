s=list(input())
n=len(s)
S=[]
t=0
while t<n-1:
    if s[t]=='B' and s[t+1]=='C':
        S.append('R')
        t+=1
    else:
        S.append(s[t])
    t+=1
if t==n-1:
    S.append(s[t])
m=len(S)
amount=0
bc=0
a=0
for i in range(m):
    if S[i]=='A':
        a += 1
    elif S[i]=='R':
        amount += a
        bc=1
    else:
        a=0
        bc=0
print(amount)