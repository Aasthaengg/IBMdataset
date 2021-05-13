from math import ceil
def roundint(num):
    fnum = float(num)
    inum = int(ceil(fnum * 0.001) * 1000)
    return inum

debt = 100000.0
n = input()
for x in xrange(n):
    debt += roundint(debt*0.05)
print int(debt)