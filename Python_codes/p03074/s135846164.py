n,k=map(int,input().split())
S=input()+"*"

A=[0] if S[0]=="1" else [0,0]
cnt,num=0,S[0]
for i in range(n+1):
    if num==S[i]:
        cnt +=1
    else:
        A.append(cnt)
        cnt=1
        num=S[i]

for i in range(1,len(A)):
    A[i]=A[i]+A[i-1]
ans=0
for i in range(0,len(A),2):
    ans=max(ans,A[min(i+k*2+1,len(A)-1)]-A[i])
print(ans)