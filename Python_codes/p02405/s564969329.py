import sys
while True:
    ins = input().split()
    h = int(ins[0])
    w = int(ins[1])
    if h == 0 and w == 0:
        break
    for i in range(h):
        for j in range(w):
            if (i + j) % 2 == 0:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')
    print("")