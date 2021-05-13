a, b = map(int, input().split())
diff = b - a
ah = sum(range(1, diff))
print(ah - a)