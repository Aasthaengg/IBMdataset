A, B, K = map(int, input().split())
for n in sorted(filter(lambda n: A <= n <= B , set(range(A, A + K)) | set(range(B - K + 1, B + 1)))):
    print(n)
