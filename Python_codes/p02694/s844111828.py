import sys
input = lambda: sys.stdin.readline().rstrip()

X = int(input())
i = 0
start = 100
while start < X:
    start += start // 100
    i += 1
print(i) 