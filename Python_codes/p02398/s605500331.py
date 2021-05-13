abc = [int(x) for x in input().split()]
a, b, c = abc[0], abc[1], abc[2]
div = [x for x in range(a, b + 1) if c % x == 0]
print(len(div))