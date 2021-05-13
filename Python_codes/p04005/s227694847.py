xyz = list(map(int, input().split()))
total = sum(xyz)
if total % 2 == 1:
    print(min(xyz) * sorted(xyz)[1])
else:
    print(0)
