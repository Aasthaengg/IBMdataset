N=int(input())
A=[]
for i in range(0,N):
    A.append(int(input()))

ans=0
for i in range(0,N-1):
    if A[i]>i:
        print(-1)
        break
    else:
        if A[i+1]>A[i]:
            if A[i+1]-A[i]>=2:
                print(-1)
                break
        else:
            ans+=A[i]
else:

    if A[N-1]>N-1:
        print(-1)
    else:
        ans+=A[-1]
        print(ans)
