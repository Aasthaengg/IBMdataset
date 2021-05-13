import sys

N = int(sys.stdin.readline())

def check(num_list):
    largest = max(num_list)
    largest_idx = num_list.index(largest)
    tmp = sum([pow(x, 2) for i, x in enumerate(num_list) if i != largest_idx])
    if tmp == pow(largest, 2):
        return "YES"
    else:
        return "NO"

for i in xrange(N):
    line = sys.stdin.readline()
    num_list = map(int, line.strip().split())
    print "{0}".format(check(num_list))