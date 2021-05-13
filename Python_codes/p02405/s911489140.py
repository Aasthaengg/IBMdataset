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
        if i == 0 or i%2 == 0:
            lever = True
        else:
            lever = False
        for j in range(x[1]):
            if lever == True:
                print("#", end = '')
                lever = False
            else:
                print(".", end ='')
                lever = True
        print("")
    print("")