N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
if N > K:
    print(sum(H[:N - K]))
else:
    print(0)