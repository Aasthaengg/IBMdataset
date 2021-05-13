import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = readline().decode().rstrip()
cnt = 0
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        cnt += 1
print(cnt)