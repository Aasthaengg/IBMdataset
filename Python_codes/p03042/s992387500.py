a, b = divmod(int(input()), 100)
x = "MM" if 0 < a < 13 else "YY"
y = "MM" if 0 < b < 13 else "YY"
print(x + y if x != y else "NA" if x == "YY" else "AMBIGUOUS")
