import sys

n = input()
x = {}

for i in range(1,5):
    for j in range(1,4):
        for k in range(1,11):
            x[(i,j,k)] = 0

for i in range(n):
    b, f, r, v = map(int, raw_input().split())
    x[(b,f,r)] += v

for i in range(1,5):
    for j in range(1,4):
        for k in range(1,11):
            sys.stdout.write(' ')
            sys.stdout.write(str(x[(i,j,k)]))
        print
    if(i != 4):
        for l in range(20):
            sys.stdout.write('#')
        print
exit(0)