N, K = map(int, input().split())
A = list(map(int, input().split()))

if (N-1)%(K-1) == 0:
    print(int((N-1)/(K-1)))
else:
    print(int((N-1)/(K-1)) + 1)