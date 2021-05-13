N,M,X=map(int,input().split())
A=list(map(int,input().split()))

s=[0 for i in range(N)]
for i in range(M):
    s[A[i]]=1
    
for i in range(X):
    cnt_0=sum(s[:X])

for j in range(N-X):
    cnt_N=sum(s[X:])

print(min(cnt_0,cnt_N))