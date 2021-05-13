n,a,b,c=map(int,input().split())
L=[]

def base10to(n,b):
    if n//b:
        return base10to(n//b,b)+str(n%b)
    return str(n%b)

for i in range(n):
    L.append(int(input()))
ans=10**10
for i in range(4**n):
    S=base10to(i,4)
    S=S.zfill(n)
    A=[]
    B=[]
    C=[]
    for j in range(n):
        if S[j]=='0':
            continue
        elif S[j]=='1':
            A.append(L[j])
        elif S[j]=='2':
            B.append(L[j])
        else:
            C.append(L[j])
    if A and B and C:
        ans=min(ans,abs(a-sum(A))+(len(A)-1)*10+abs(b-sum(B))+(len(B)-1)*10+abs(c-sum(C))+(len(C)-1)*10)
print(ans)