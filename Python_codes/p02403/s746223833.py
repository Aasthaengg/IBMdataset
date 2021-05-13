def printRect(h,w):
    for i in range(h):
        print("#"*w)

while True:
    l = [int(i) for i in input().split(' ')]
    if l[0] == 0 and l[1] == 0:
        break
    else:
        printRect(l[0],l[1])
        print()