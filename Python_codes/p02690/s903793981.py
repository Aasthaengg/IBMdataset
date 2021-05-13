x = int(input())
count =0
for a in range(-200, 200):
    for b in range(-200, 200):
        if a**5 - b**5 == x:
            A = a
            B = b

print(A, B)