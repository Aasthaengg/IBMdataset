N,K = map(int,input().split())
A = list(map(int,input().split()))
grade=[]
oldest=[]
result = [0] * (N+1-K)
for i in range(K,N+1):
    oldest.append(A[i-K])
    if i!=K:
        if A[i-1] > oldest[i-K-1]:
            print("Yes")
        else:
            print("No")