import sys

input = sys.stdin.readline
x = [0, 0, 0]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a += max(x[1], x[2])
    b += max(x[0], x[2])
    c += max(x[0], x[1])
    x = [a, b, c]
print(max(x))