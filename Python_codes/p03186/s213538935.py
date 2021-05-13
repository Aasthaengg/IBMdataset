a, b, c = map(int, input().split())
print(b + c - (c-1-b) + min(c-1-b, a))