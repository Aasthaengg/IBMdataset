import sys
s = sys.stdin.readline().rstrip("\n")
i = 0
ans = ''
for m in s:
    if i % 2 == 0:
        ans += m
    i += 1
print(ans)