a, b = map(int, input().split())
diff = b - a
h = (diff-1) * diff // 2
print(h - a)