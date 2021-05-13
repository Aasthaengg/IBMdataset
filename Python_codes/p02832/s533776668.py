N=int(input())
A=list(map(int,input().split()))
x,cnt=1,0

for i in range(N):
    if A[i]==x:
        x+=1
    else:
        cnt+=1

if cnt==N:
    cnt=-1
    
print(cnt)