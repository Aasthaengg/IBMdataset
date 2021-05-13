import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
i = 0
cnt = 0
while i <= 2:
  cnt += 1 if a[i] == b[i] else 0
  i += 1
print(cnt)
