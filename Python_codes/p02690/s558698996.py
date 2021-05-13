X = int(input())

for a in range(200):
    for b in range(-200, 1):
        if a**5-b**5==X:
            print(str(a) + " " + str(b))
            exit()

a = 0
b = 0

while True:
    cand = a**5-b**5
    if cand == X:
        print(str(a) + " " + str(b))
        exit()
    elif cand < X:
        a += 1
    else:
        b += 1