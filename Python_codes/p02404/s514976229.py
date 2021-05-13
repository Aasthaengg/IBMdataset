matrix = []
while True:
    values = input()
    if '0 0' == values:
        break
    matrix.append([int(x) for x in values.split()])

for height, width in matrix:
    for i in range(height):
        if 0 == i or height - 1 == i:
            print('#' * width)
        else:
            print('{0}{1}{2}'.format('#', '.' * (width - 2), '#'))
    print()