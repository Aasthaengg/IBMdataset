n, h, w = map(int, input().split())
print(sum(h <= a and w <= b for a, b in (map(int, input().split()) for _ in range(n))))
