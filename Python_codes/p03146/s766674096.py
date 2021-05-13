a = int(input())

A = []

while a not in A:
    A.append(a)
    if a%2 == 0:
        a = a//2
    else:
        a = 3*a + 1

print(len(A) + 1)