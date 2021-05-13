def solve():
    s = input()
    a = int(s[:2])
    if a == 0 or a > 12:
        x = "YY"
    else:
        x = "MM"
    b = int(s[2:])
    if b == 0 or b > 12:
        y = "YY"
    else:
        y = "MM"
    if x + y == "YYYY":
        print("NA")
    elif x + y == "MMMM":
        print("AMBIGUOUS")
    else:
        print(x + y)


solve()
