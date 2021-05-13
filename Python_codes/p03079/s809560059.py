x = input()
inputs = x.split()
a, b, c = int(inputs[0]), int(inputs[1]), int(inputs[2])

if a == b and b == c:
    print('Yes')
else:
    print('No')
