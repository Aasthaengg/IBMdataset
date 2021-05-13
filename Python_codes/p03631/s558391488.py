import sys
input = sys.stdin.readline().rstrip
n = input()
print('Yes' if n == n[::-1] else 'No')