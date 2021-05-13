N, K = map(int, input().split())
H = list(map(int, input().split()))

print(sum([1 if h >= K else 0 for h in H]))