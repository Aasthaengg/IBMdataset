N,K = [int(i)for i in input().split()]
A = [int(i) for i in input().split()]

for i in range(K,N):
    if A[i] / A[i-K] > 1 :
        print("Yes")

    else :
        print("No")