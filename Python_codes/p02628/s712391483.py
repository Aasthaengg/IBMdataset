n, k = map(int, input().split())
p1 = list(map(int, input().split()))
p2 = sorted(p1)
p3 = sum(p2[:k])
print(p3)