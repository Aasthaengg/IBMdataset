import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[a[i]-1] == i + 1:
        cnt += 1
print(cnt//2)