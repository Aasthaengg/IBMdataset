import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b = map(int, readline().split())

ans = []
for i in range(a, b+1):
    if str(i) == str(i)[::-1]:
        ans.append(i)
print(len(ans))