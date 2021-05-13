K,N=map(int,input().split())
A=list(map(int,input().split()))
now=0
sp=[A[0]+(K-A[-1])]

for i in range(N):
    sp.append(abs(now-A[i]))
    now=A[i]

print(K-max(sp))