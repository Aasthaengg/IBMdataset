N=int(input())
A=list(map(int,input().split()))
if N==1:
    print(1)
    exit()

B=[A[i]-A[i-1] for i in range(1,N)]
ans=0
flag=False
for i in range(N-1):
    if B[i]!=0:
        first=B[i]
        flag=True
    if flag:
        break
for i in range(N-1):
    if first*B[i]>=0:
        pass
    else:
        ans+=1
        j=i+1
        while j<=N-2:
            if B[j]!=0:
                first=B[j]
                break
            else:
                j+=1

print(ans+1)