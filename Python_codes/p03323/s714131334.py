line = input()
a, b = [int(n) for n in line.split()]

if a > 8 or b > 8:
    print(":(")

elif a == b or a < b or b < a:
    print("Yay!")

