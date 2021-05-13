X, Y = map(int, input().split())

A = []
a = X

while 1:
    A.append(a)
    if a*2 > Y:
        break
    a *= 2

print(len(A))
