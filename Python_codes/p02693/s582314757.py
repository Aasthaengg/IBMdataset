import sys
input = sys.stdin.readline

k, (a, b) = int(input()), tuple(map(int, input().split()))
print('OK' if a <= (b // k) * k else 'NG')