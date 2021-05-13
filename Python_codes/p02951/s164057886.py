a, b, c = map(int, input().split())
# print(a)
d = a-b
print(0 if d > c else c-d)
