n, a, b = map(int, input().split())
d = max(a, b) - min(a, b) - 1
if d & 1:
    print("Alice")
else:
    print("Borys")