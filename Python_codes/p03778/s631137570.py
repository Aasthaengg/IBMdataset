w, a, b = map(int, input().split())
l = [0, b - a - w, a - b - w, 0]
print(l[(a + w < b) + ((b + w < a) << 1)])