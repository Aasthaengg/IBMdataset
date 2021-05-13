A, B, K = list(map(int, input().split()))

if A + K > B - K:
    for num in range(A, B + 1):
        print(num)
else:
    for num in range(A, A + K):
        print(num)
    for num in range(B - K + 1, B + 1):
        print(num)