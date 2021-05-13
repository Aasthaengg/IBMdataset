N, A, B = map(int, input().split())
if (B - A) & 1:
    print("Borys")
else:
    print("Alice")