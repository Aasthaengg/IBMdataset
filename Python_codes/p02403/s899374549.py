import sys
while 1 > 0:
    height, width = map(int, raw_input().split())
    if height == 0 and width == 0:
        break
    for i in range(height):
        for j in range(width):
            sys.stdout.write("#")
        print ""
    print ""