import sys

s = sys.stdin.readline().replace('\n','')
t = sys.stdin.readline().replace('\n','')
res = 0
for i in range(len(s)):
    if s[i] != t[i]: res += 1

print(res)
