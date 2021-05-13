from itertools import permutations
a = list(map(int, input()))

op = ['+', '+', '+', '-', '-', '-']
for ops in permutations(op, 3):
    now = a[0]
    for i in range(3):
        if ops[i] == '+':
            now += a[i+1]
        else:
            now -= a[i+1]
    if now == 7:
        print("{}{}{}{}{}{}{}=7".format(
            a[0], ops[0], a[1], ops[1], a[2], ops[2], a[3]))
        exit()
