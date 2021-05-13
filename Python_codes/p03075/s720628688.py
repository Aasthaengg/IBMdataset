a = [int(input()) for _ in range(6)]

if a[-2] - a[0] > a[-1]:
    print(":(")
else:
    print("Yay!")