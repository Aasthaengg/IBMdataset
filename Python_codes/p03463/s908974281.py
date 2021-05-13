row = list(map(int, input().split()))

if (row[2] - row[1]) % 2 == 1:
    print("Borys")
else:
    print("Alice")