s = input()
a, b, c, d = map(int, s)
A, B, C, D = map(str, s)
x = "=7"
if a + b + c + d == 7:
    print(A + "+" + B + "+" + C + "+"+D + x)
elif a - b + c + d == 7:
    print(A + "-" + B + "+" + C + "+"+D + x)
elif a + b - c + d == 7:
    print(A + "+" + B + "-" + C + "+"+D + x)
elif a + b + c - d == 7:
    print(A + "+" + B + "+" + C + "-" + D + x)
elif a - b - c + d == 7:
    print(A + "-" + B + "-" + C + "+" + D + x)
elif a - b + c - d == 7:
    print(A + "-" + B + "+" + C + "-" + D + x)
elif a + b - c - d == 7:
    print(A + "+" + B + "-" + C + "-" + D + x)
elif a - b - c - d == 7:
    print(A + "-" + B + "-" + C + "-" + D + x)
