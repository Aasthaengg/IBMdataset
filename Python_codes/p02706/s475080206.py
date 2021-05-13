N, M = map(int, input().split())
acc = sum(map(int, input().split()))
print(N - acc if N - acc >= 0 else -1)
