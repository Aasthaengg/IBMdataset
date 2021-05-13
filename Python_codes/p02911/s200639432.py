N,K,Q=map(int,input().split())

D=[0]*(N+1)
for _ in range(Q):
    D[int(input())]+=1

for i in range(1,N+1):
    if K+D[i]-Q>0:
        print("Yes")
    else:
        print("No")
