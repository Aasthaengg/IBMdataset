def battle():
    a, b, c, d = map(int, input().split())
    while a > 0 or c > 0:
        c = c - b
        if c <= 0:
            return "Yes"
        a = a - d
        if a <= 0:
            return "No"

rst = battle()
print(rst)