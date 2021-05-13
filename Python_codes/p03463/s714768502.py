n, a, b = map(int, input().split())
diff = b - a - 1
if diff%2:
    print("Alice")
elif diff%2 == 0:
    print("Borys")
else:
    print("Draw")
