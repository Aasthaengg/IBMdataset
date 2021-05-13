import sys
a, b = list(map(int, sys.stdin.readline().strip().split(' ')))
sys.stdout.write(str(max(a+b, a-b, a*b)) + '\n')

# test