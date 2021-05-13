a, b, c = map(int, input().split())
bc = b + c

if bc > a:
    bc -= a
    print(bc)
else:
    print("0")
