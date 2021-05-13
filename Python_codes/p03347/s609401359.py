n=int(input())
A=[int(input()) for _ in range(n)]

if A[0]!=0:print(-1);exit()

cnt=0
for i in range(1,n):
    if A[i-1]+1==A[i]:
        cnt +=1
    elif A[i-1]==A[i] or A[i-1]>A[i]:
        cnt +=A[i]
    else:print(-1);exit()

print(cnt)