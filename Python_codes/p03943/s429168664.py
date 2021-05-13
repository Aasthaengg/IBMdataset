c = sorted(list(map(int, input().split())))
if c[2] != c[0] + c[1]:
    print("No")
else:
    print("Yes")