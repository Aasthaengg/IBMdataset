A, B = map(int, input().split())
cal = A - B * 2
if cal >= 0:
    print(cal)
else:
    print(0)