line = raw_input()
n, k = [int(s) for s in line.split(' ')]
print 0 if n % k == 0 else 1
