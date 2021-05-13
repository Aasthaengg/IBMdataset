n, k = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)
l = l[::-1]
print(sum(l[:k]))