A =int(input())
B =int(input())

D =[1,2,3]


if A in D:
    D.remove(A)

if B in D:
    D.remove(B)

print(D[0])
