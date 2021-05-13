N, K = map(int, input().split())
h = list(map(int, input().split()))
H = list(1 for x in h if x >= K)
print(sum(H))