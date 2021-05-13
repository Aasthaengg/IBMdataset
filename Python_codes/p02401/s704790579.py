import sys

s = sys.stdin.readlines()
for i in s:
    if '?' in i:
        break
    print(eval(i.replace('/', '//')))