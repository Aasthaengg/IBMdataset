N,M=map(int,input().split())
ans=[]

if N%2==0:
    N-=1

half=N//2

if half%2==0:
    for i in range(half//2):
        ans.append((i+1,half-i))
    for j in range(half//2):
        ans.append((half+1+j,N-j))
else:
    for i in range(half//2):
        ans.append((i+1,half-i))
    for j in range(half//2+1):
        ans.append((half+1+j,N-j))

#print(ans)
for i in range(M):
    print(*ans[i])