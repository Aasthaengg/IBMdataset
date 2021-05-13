def median(array):
    tmp = sorted(array)
    if len(array) % 2:
        return tmp[len(array)//2]
    else:
        return (tmp[len(array)//2] + tmp[len(array)//2 - 1]) / 2


[n], *x = [[*map(int, t.split())] for t in open(0)]
a, b = zip(*x)
if n % 2 == 0:
    print(int(2*(median(b) - median(a)) + 1))
else:
    print(median(b) - median(a) + 1)
