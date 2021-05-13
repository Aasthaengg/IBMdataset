x, y = map(int, input().split())

if x in [1, 3, 5, 7, 8, 10, 12]:
    x_j = 1

elif x in [2]:
    x_j = 2

elif x in [4, 6, 9, 11]:
    x_j = 3

if y in [1, 3, 5, 7, 8, 10, 12]:
    y_j = 1

elif y in [2]:
    y_j = 2

elif y in [4, 6, 9, 11]:
    y_j = 3

if (x_j == y_j):
    print("Yes")

else:
    print("No")