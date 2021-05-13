N,M=map(int,input().split())
l=[0]*M
for i in range(N):
    a=list(map(int,input().split()))
    for j in a[1:]:
        l[j-1]+=1
cnt=0
for k in l:
    if k==N:
        cnt+=1
print(cnt)