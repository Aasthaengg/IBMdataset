import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = readline().decode().rstrip()

ans = float('inf')
for i in range(len(s) - 2):
    x = int(s[i]) * 100 + int(s[i + 1]) * 10 + int(s[i + 2])
    res = abs(753 - x)
    ans = min(ans, abs(753 - x))
print(ans)
