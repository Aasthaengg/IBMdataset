N, K, *A = map(int, open(0).read().split())
for i in range(N):
    unko = A[i]
    if i + K < N:
        S = A[i + K]
        if S > unko:
            print("Yes")
        else:
            print("No")
    else:
        exit
