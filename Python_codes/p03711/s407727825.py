x, y = map(int, input().split())

A = [1, 3, 5, 7, 8, 10, 12]
B = [4, 6, 9, 11]

if x in A:
    x = "A"
elif x in B:
    x = "B"
else:
    x = "C"

if y in A:
    y = "A"
elif y in B:
    y = "B"
else:
    y = "C"

if x == y:
    print("Yes")
else:
    print("No")