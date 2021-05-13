x, y = map(int, input().split())

A = [1, 3, 5, 7, 8, 10, 12]
B = [4, 6, 9, 11]
C = [2]
a = 0
if x in A and y in A:
    a = 1
else:
    if x in B and y in B:
        a = 1
    else:
        if x in C and y in C:
            a = 1

if a == 1:
    print("Yes")
else:
    print("No")
