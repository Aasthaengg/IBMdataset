A, B, C = map(int, input().split())
total = C-(A-B)
if total <= 0:
    print(0)
else:
    print(total)
