x = int(input())
if x == 1:
    print("Hello World")
    exit()
if x == 2:
    y, z = [int(input()) for _ in range(2)]
    print(y + z)
