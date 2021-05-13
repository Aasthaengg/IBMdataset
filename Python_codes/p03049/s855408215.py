N=int(input())
A=0
B=0
C=0
ans=0
for _ in range(0,N):
    s=input()
    if s[0]=='B':
        B+=1
    if s[-1]=='A':
        A+=1
    if s[-1]=='A' and s[0]=='B':
        C+=1

    for i in range(0,len(s)-1):
        if s[i]=='A' and s[i+1]=='B':
            ans+=1

if A!=C or B!=C:
    print(ans+min(A,B))
else:
    if A==0:
        print(ans)
    else:
        print(ans+C-1)

