n,q = map(int,input().split())
s=input()
LR=[]
for i in range(q):
    l,r = map(int,input().split())
    LR.append([l,r])

c=0
p=0
C=[]
for i in range(len(s)):
    if s[i]=="A":
        p=1
    elif p==1 and s[i]=="C":
        c+=1
        p=0
    else:
        p=0
    C.append(c)

for i in range(q):
    l=LR[i][0]
    r=LR[i][1]
    ans = C[r-1]-C[l-1]
    print(ans)