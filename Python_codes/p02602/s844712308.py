N, K = map(int, input().split())
An = list(map(int, input().split()))
Bn = []
Bn.append(0)
for i in range(N):
    Bn.append(An[i]+Bn[i])
for i in range(K+1, N+1):
    if (Bn[i]-Bn[i-K] > Bn[i-1]-Bn[i-K-1]):
        print("Yes")
    else:
        print("No")

