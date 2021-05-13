line = input()
tokens = line.split(' ')
a, b, c = int(tokens[0]), int(tokens[1]), int(tokens[2])
if a == b and b == c:
    print('Yes')
else:
    print('No')
