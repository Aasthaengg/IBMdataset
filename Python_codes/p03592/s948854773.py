N,M,K=map(int,input().split())

cand=[]
for i in range(N+1):
    for j in range(M+1):
        cand.append(i*(M-j)+j*(N-i))

if K in cand:
    print("Yes")
else:
    print("No")