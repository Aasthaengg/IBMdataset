from itertools import product as P

a, b, c, d = input()

ops = P(("+", "-"), repeat=3)
for op1, op2, op3 in ops:
    f = f"{a}{op1}{b}{op2}{c}{op3}{d}"
    if eval(f) == 7:
        print(f + "=7")
        break