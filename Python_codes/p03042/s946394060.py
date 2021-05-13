s = int(input())
a, b = s // 100, s % 100
x = "YY" if a == 0 or a > 12 else "MM"
y = "YY" if b == 0 or b > 12 else "MM"
if x != y:
    print(x + y)
else:
    print("NA" if x == "YY" else "AMBIGUOUS")
