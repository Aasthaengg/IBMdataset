n,k=map(int,input().split())
S=input()

now=S[0]
cnt=1
A=[] #個数配列
for i in range(n-1):
    if S[i+1]==now:
        cnt+=1
    else:
        A.append(cnt)
        cnt=1
        now=S[i+1]
if cnt>0:
    A.append(cnt)
l=len(A)
    
if S[0]=="0":
    if l<=2*k:
        ans=n
    elif 2*k+1<=l<=2*k+2:
        ans=max(sum(A[:2*k]),sum(A[1:]))
    else:
        ans=max(sum(A[:2*k]),sum(A[1:2*k+2]))
        cnt=sum(A[1:2*k+2])
        for i in range((l-2*k-2)//2):
            cnt-=A[2*i+1]+A[2*i+2]
            cnt+=A[2*k+2*i+2]+A[2*k+2*i+3]
            ans=max(cnt,ans)
        if l%2!=0:
            ans=max(sum(A[l-2*k:]),ans)
else:
    if l<=2*k+1:
        ans=n
    else:
        ans=sum(A[:2*k+1])
        cnt=ans
        for i in range((l-2*k-1)//2):
            cnt-=A[2*i]+A[2*i+1]
            cnt+=A[2*k+2*i+1]+A[2*k+2*i+2]
            ans=max(cnt,ans)
        if l%2==0:
            ans=max(sum(A[l-2*k:]),ans)
print(ans)