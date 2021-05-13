a, b, c = [int(x) for x in raw_input().split(" ")]

if a < b and b < c:
    print("Yes")
else:
    print("No")