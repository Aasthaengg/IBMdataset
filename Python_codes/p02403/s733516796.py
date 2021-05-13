rectArray = []

h, w = input().split()
h = int(h)
w = int(w)

while h != 0 and w != 0:
    rectArray.append([h, w])
    h, w = input().split()
    h = int(h)
    w = int(w)

for x in rectArray:
    for i in range(x[0]):
        for j in range(x[1]):
            print("#", end = '')
        print("")
    print("")