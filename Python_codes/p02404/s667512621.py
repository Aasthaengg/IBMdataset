import sys
a = []
while True:
    x = map(int, raw_input().split())
    if x[0] == 0 and x[1] == 0:
        break
    a.append(x)
for i in range(len(a)):
    for j in range(a[i][0]):
        if j == 0 or j == (a[i][0]-1):
            for k in range(a[i][1]):
                sys.stdout.write('#')
        else:
            sys.stdout.write('#')
            for k in range(a[i][1]-2):
                sys.stdout.write('.')
            sys.stdout.write('#')
        print ''
    print ''