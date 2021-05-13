N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
if 0 < K < N:
    print(sum(H[:-K]))
elif K == 0:
    print(sum(H))
else:
    print(0)