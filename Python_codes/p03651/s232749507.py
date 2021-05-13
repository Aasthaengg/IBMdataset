N, K = map(int, input().split())
A = list(map(int, input().split()))
max_A = max(A)
A.sort()

if(max_A < K):
    print("IMPOSSIBLE")
else:
    num = 10**10
    for i in range(N-1):
        if(min(num, abs(A[i]-A[i+1]))):
            num = min(num, abs(A[i]-A[i+1]))

    for i in range(N):
        if(A[i] < K):
            continue
        if((K-A[i])%num == 0):
            print("POSSIBLE")
            break
    else:
        print("IMPOSSIBLE")