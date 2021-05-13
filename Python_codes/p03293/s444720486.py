import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s, t = read().decode().rstrip().split()
ans = 'No'
for i in range(len(s)):
    s = s[-1]+s[:-1]
    if s == t:
        ans = 'Yes'
        continue
print(ans)
