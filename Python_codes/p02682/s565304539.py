A, B, C, K = map(int, input().split())


if 0 < K <= A:
    print(K)
elif A < K < A + B:
    print(A)
else:
    C_num = K - (A + B)
    print(A - C_num)
