line = input()
a, b = [int(n) for n in line.split()]

if a>=b:
    c = a/2
    d = 16-a
    if c>d or a>8:
        print(":(")
    else:
        print("Yay!")
else:
    c = b/2
    d = 16 -b
    if c>d or b>8:
        print(":(")

    else:
        print("Yay!")

