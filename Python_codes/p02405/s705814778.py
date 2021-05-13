import sys


while True:
    j = 1
    h,w = map(int,raw_input().split())
    if h == 0 and w == 0:
        break
    while j <= h:
        i = 1
        if j % 2:
            while i <= w:
                if i % 2:
                    sys.stdout.write("#")
                elif not i % 2:
                    sys.stdout.write(".")
                if not i % w:
                    sys.stdout.write("\n")
                i +=1
        if not j % 2:
            while i <= w:
                if i % 2:
                    sys.stdout.write(".")
                elif not i % 2:
                    sys.stdout.write("#")
                if not i % w:
                    sys.stdout.write("\n")
                i +=1
        j += 1
    sys.stdout.write("\n")