N, K = map(int, input().split())

if K == 1:
    print(0)
else:
    print(abs(1-(N-K+1)))