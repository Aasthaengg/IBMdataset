n = int(input())

d2 = n % 100
u2 = n // 100

if 1 <= d2 <= 12 and 1 <= u2 <= 12:
    print("AMBIGUOUS ")
elif 1 <= d2 <= 12:
    print("YYMM")
elif 1 <= u2 <= 12:
    print("MMYY")
else:
    print("NA")
