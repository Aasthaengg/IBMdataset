N,x=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
cnt=0
for i in range(N-1):
    x-=A[i]
    if x >= 0:
        cnt+=1
    else:
        break
if x==A[N-1]:
    cnt+=1
print(cnt)