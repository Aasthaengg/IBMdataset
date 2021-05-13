n = int(input())
i = 0

while True:
    x = n+i
    x = str(x)
    if x[0] == x[1] and x[1] == x[2]:
        print (x)
        exit ()
    else:
        i += 1
