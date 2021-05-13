import sys

n = int(input())
dic = set()

for i in range(n):
    c, s = sys.stdin.readline().split()
    if c == 'insert':
        dic.add(s)
    else:
        if s in dic:
            print('yes')
        else:
            print('no')