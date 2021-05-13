x, a, b = map(int, input().split())
if a < b:
    c = ["A", "B"]
else:
    c = ["B", "A"]
print(c[0] if x < (a + b) / 2 else c[1])