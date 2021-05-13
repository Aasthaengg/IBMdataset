X = int(input())

going = False

for A in range(-120, 121):
    for B in range(-120, 121):
        if A ** 5 - B ** 5 == X:
            print(A, B)
            going = True
            break
    if going:
        break
