A = int(input())
B = int(input())
C = int(input())
X = int(input())

counter = 0

for ai in range(A + 1):
    for bi in range(B + 1):
        for ci in range(C + 1):
            if X == ai * 500 + bi * 100 + ci * 50:

                counter += 1

print(counter)