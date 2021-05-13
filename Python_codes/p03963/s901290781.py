import itertools
N,K=map(int,input().split())
ans=1
flag=True

for i in range(N):
    if flag:
        ans*=K
        flag=False
    else:
        ans*=(K-1)

print(ans)