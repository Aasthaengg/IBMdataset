x = int(input())
a = x // 100
b = x % 100

a_is_month = 0 < a & a <= 12
b_is_month = 0 < b & b <= 12

if a_is_month:
    if b_is_month:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if b_is_month:
        print("YYMM")
    else:
        print("NA")

