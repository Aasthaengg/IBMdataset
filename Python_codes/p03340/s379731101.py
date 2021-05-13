n=int(input())
A=list(map(int,input().split()))
L=0
R=0
now=A[0]
add=0
flag=0 #越しているなら1
Ans=[]
while R<n-1:
    if flag==0:
        R+=1
        if now+A[R]==now^A[R]:
            now+=A[R]
        else:
            Ans.append([L,R-1])
            flag=1
    else:
        now-=A[L]
        L+=1
        if now+A[R]==now^A[R]:
            now+=A[R]
            flag=0
if flag==0:
    Ans.append([L,R])
else:
    while L<n-1:
        now-=A[L]
        L+=1
        if now+A[R]==now^A[R]:
            Ans.append([L,R])

#print(Ans)
ans=0
for i in range(len(Ans)):
    d=Ans[i][1]-Ans[i][0]+1
    ans+=(d+1)*d//2
    if i!=0:
        d=Ans[i-1][1]-Ans[i][0]+1
        if d>0:
            ans-=(d+1)*d//2
print(ans)