N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
cumlsum=[0]*N
su=0
for i in range(N):
    su=su+A[N-1-i]
    cumlsum[N-1-i]=su
#print(A,cumlsum)
cnt=1
for i in range(1,N,1):
    #print(A[i-1],cumlsum[i])
    if A[i-1]/2<=cumlsum[i]:
        cnt=cnt+1
    else:
        break
print(cnt)