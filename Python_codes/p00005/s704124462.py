import fileinput


def GCD(x, y):
    if y != 0:
        return GCD(y, x % y)
    else:
        return x

for line in fileinput.input():
    x, y = [int(s) for s in line.split()]
    #print("{} {}".format(GCD(x, y), int(x * y/GCD(x, y))))#別にformatでなくてもいい
    print(GCD(x, y),int(x * y/GCD(x, y)))
