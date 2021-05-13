a, b, c = map(int, input().split())

left = a - b
print(max(0, c - left))
