import sys
input = sys.stdin.readline

x, b, res = int(input()), 100, 0
while b < x: b += b // 100; res += 1
print(res)