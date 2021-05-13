N=int(input())
A=list(map(int,input().split()))
Min=min(A)
Max=max(A)
if Min>=0:
    cnt=N-1
    ans=[]
    for i in range(1,N):
        ans.append((i,i+1))
elif Max<=0:
    cnt=N-1
    ans=[]
    for i in range(N-1,0,-1):
        ans.append((i+1,i))
else:
    if abs(Min)>=abs(Max):
        idx=A.index(Min)
        ans=[]
        cnt=2*N-1
        for i in range(N):
            ans.append((idx+1,i+1))
        for i in range(N-1,0,-1):
            ans.append((i+1,i))
    elif abs(Min)<abs(Max):
        idx=A.index(Max)
        ans=[]
        cnt=2*N-1
        for i in range(N):
            ans.append((idx+1,i+1))
        for i in range(1,N):
            ans.append((i,i+1))
print(cnt)
for i in range(cnt):
    print(str(ans[i][0])+' '+str(ans[i][1]))