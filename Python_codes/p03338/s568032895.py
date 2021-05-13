import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
s = readline().decode().rstrip()
ans = 0
for i in range(1, n):
    cnt = 0
    for j in set(s[:i:]):
        if j in set(s[i::]):
            cnt += 1
    ans = max(ans, cnt)
print(ans)
