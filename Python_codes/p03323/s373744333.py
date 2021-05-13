a, b = map(int, input().split())
if a <= 8:
    if b <= 8:
        print("Yay!")
    else:
        print(":(")
elif b <= 8:
    if a <= 8:
        print("Yay!")
    else:
        print(":(")