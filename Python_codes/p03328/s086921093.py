a, b = map(int, input().split())
diff = b - a
snow = diff * (diff + 1) // 2 - b
print(snow)
