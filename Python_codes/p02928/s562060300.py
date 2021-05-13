N,K,*A=map(int,open(0).read().split())
a=0
b=0
for i in range(N):
    for j in range(N):
        if A[j]>A[i]:
            a+=1
            if j<i:b+=1
print((b*K+a*K*(K-1)//2)%(10**9+7))
