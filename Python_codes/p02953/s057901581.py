import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

n, *h = map(int, read().split())

if n == 1:
    print("Yes")
    exit()

for i in range(n-2, 0, -1):
    if h[i] >= h[i+1] + 2:
        print("No")
        exit()
    elif h[i] > h[i+1]:
        h[i] -= 1

print("Yes")
