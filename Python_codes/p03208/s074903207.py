N, K = list(map(lambda k: int(k), input().split(" ")))
H = [int(input()) for i in range(N)]
H.sort()

print(min([H[i + K - 1] - H[i] for i in range(len(H) - K + 1)]))