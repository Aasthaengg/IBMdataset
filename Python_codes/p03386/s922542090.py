A, B, K = map(int, input().split())
if A + K - 1 >= B - K + 1:
    print("\n".join(map(str, [i for i in range(A, B + 1)])))
else:
    print("\n".join(map(str, [i for i in range(A, A + K)])))
    print("\n".join(map(str, [i for i in range(B - K + 1, B + 1)])))
