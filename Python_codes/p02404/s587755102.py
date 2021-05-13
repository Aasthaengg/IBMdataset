a, b = (int(i) for i in input().split())
while a != 0 and b != 0:
    cow = '#'
    for i in range(1, b):
        cow += '#'
    print('{0}'.format(cow))
    for i in range(1, a-1):
        row = '#'
        for j in range(1, b-1):
            row += '.'
        row += '#'
        print('{0}'.format(row))
    cow = '#'
    for i in range(1, b):
        cow += '#'
    print('{0}'.format(cow))
    print()
    a, b = (int(i) for i in input().split())