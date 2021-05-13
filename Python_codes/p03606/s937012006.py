N=int(input())
K=0
for i in range(N):
    l,r = map(int,input().split())
    K=(r-l+1)+K
print(K)