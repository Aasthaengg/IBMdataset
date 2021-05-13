import sys
while True:
    a,b = map(int, raw_input().split())
    if a ==0 and b == 0:
        break
    for i in range(a):
        for j in range(b):
            if (i % 2 == 0 and j % 2 == 0) or ( i % 2 == 1 and j % 2 == 1):
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        print 
    print