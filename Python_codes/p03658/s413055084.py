N, K = map(int, input().split())
L = list(map(int, input().split()))
sorted_L = sorted(L, reverse=True)
print(sum(sorted_L[:K]))
