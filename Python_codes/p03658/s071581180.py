n, k = map(int, input().split())
ns = list(map(int, input().split()))
ns = sorted(ns)
print(sum(ns[-k:]))