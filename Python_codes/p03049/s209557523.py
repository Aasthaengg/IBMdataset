n=int(input())
s=[input() for i in range(n)]
count=0
A=0
B=0
BA=0
for i in range(n):
    for j in range(len(s[i])-1):
        if j==0:
            if s[i][j]=='B':
                B+=1
        if j==len(s[i])-2:
            if s[i][j+1]=='A':
                A+=1
        if s[i][j:j+2]=='AB':
            count+=1
    if s[i][0]=='B' and s[i][-1]=='A':
        BA+=1
        A-=1
        B-=1

if BA==0:
    print(count+min(A,B))
else:
    ans=count+BA-1
    if A>=1 and B>=1:
        print(ans+2+min(A,B)-1)
    elif A>=1 or B>=1:
        print(ans+1)
    else:
        print(ans)