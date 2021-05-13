a, b = map(int, input().split())

if a >= -1000 and b <= 1000:
    if a < b:
        print("a < b", end="\n")
    elif a > b:
        print("a > b", end="\n")
    elif a == b:
        print("a == b", end="\n")