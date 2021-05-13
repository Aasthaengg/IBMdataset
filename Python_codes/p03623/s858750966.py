x, a, b = map(int, (input().split()))

if a < x:
    a_abs = x-a
else:
    a_abs = a-x

if b < x:
    b_abs = x-b
else:
    b_abs = b-x
if a_abs > b_abs:
    print("B")
else:
    print("A")