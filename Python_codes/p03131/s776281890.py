K, A, B = map(int, input().split())
if A >= B-1:
    print(K+1)
else:
    if K <= A-1:
        print(K+1)
    else:
        K -= A-1
        print(A + (B-A)*(K//2) + [1,0][K%2 == 0])