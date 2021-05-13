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
            if i == 0 or j == 0 or i == x[0] - 1 or j == x[1] - 1:
                print("#", end = '')
            else:
                 print(".", end ='')
        print("")
    print("")