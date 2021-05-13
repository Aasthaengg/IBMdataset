import sys

n = input()
a = map(int, raw_input().split())

for i in xrange(n - 1):
    tmp = str(a[len(a) - i - 1]) + ' '
    sys.stdout.write(tmp)
    
print "%d" % a[0]