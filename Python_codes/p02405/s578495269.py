import sys
a = []
while True:
    x = map(int, raw_input().split())
    if x[0] == 0 and x[1] == 0:
        break
    a.append(x)
for i in range(len(a)):
    for j in range(a[i][0]):
        if j%2 == 0:
            for k in range(a[i][1]):
                if k%2 == 0:
                    sys.stdout.write('#')
                else:
                    sys.stdout.write('.')
        else:
            for k in range(a[i][1]):
                if k % 2 == 0:
                    sys.stdout.write('.')
                else:
                    sys.stdout.write('#')
        print ''
    print ''