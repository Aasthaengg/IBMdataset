import sys
import copy
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(input().strip())
s = input().strip()
ans = 0
cnt = 0
for i in s:
    if i == "I": cnt += 1 
    else: cnt -= 1
    ans = max(ans, cnt)
print(ans)
