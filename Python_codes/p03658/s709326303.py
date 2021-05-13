N, K = map(int, input().split())
length = sorted(map(int, input().split()), reverse=True)
print(sum(length[:K]))
