A, B = map(int, input().split(" "))

if any(map(lambda x: x % 3 == 0, (A, B, A + B))):
    print("Possible")
else:
    print("Impossible")
