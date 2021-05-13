a, b, c, d = [int(x) for x in input().strip()]
if a + b + c + d == 7:
    print(f"{a}+{b}+{c}+{d}=7")
elif a + b + c - d == 7:
    print(f"{a}+{b}+{c}-{d}=7")
elif a + b - c + d == 7:
    print(f"{a}+{b}-{c}+{d}=7")
elif a - b + c + d == 7:
    print(f"{a}-{b}+{c}+{d}=7")
elif a - b - c + d == 7:
    print(f"{a}-{b}-{c}+{d}=7")
elif a + b - c - d == 7:
    print(f"{a}+{b}-{c}-{d}=7")
elif a - b + c - d == 7:
    print(f"{a}-{b}+{c}-{d}=7")
elif a - b - c - d == 7:
    print(f"{a}-{b}-{c}-{d}=7")
