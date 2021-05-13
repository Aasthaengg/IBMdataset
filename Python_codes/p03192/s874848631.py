import sys

line = sys.stdin.readline().replace('\n', '')

cnt = 0
for i in line:
  if i == '2':
    cnt += 1

print (cnt)