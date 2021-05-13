import sys
while True:
    a,b = map(int, raw_input().split())
    if a ==0 and b == 0:
        break
    for i in range(a):
        for j in range(b):
            sys.stdout.write("#")
        print 
    print