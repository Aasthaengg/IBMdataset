N,K=map(int,input().split())
A=list(map(int,input().split()))
cnt=0
for i in range(10**5+1):
    N-=K
    cnt+=1
    if N<=0:
        break
    else:
        N+=1
print(cnt)   