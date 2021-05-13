import sys

w = input()
s = []
cnt = 0

for i in sys.stdin.readlines():
    if i == 'END_OF_TEXT\n':
        break
    for j in [x.strip('.').lower() for x in i.split()]:
        s.append(j)

for i in s:
    if w == i:
        cnt += 1

print(cnt)