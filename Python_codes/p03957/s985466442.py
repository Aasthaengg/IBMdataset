s=input()
try:
    A = s.index("C")
except ValueError:
    print("No")
    exit()
try:
    B = s[A:].index("F")
    print("Yes")
except ValueError:
    print("No")
    exit()