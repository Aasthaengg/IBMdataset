import sys
n , m = [int(i) for i in sys.stdin.readline().split()]
res = 1900 * m + 100 * (n - m)
print(res * 2 ** m)