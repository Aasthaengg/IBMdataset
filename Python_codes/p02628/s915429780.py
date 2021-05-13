n, k = map(int, input().split())
p = list(map(int, input().split()))
l = sorted(p)

s = sum(l[:k])
print(s)
