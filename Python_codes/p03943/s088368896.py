a, b, c = map(int, input().split())

add = a + b + c
big = max(a, b, c)

if add == big * 2:
    print("Yes")

else:
    print("No")
