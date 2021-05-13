import sys

n = int(input())
dic = {}

for i in range(n):
    c, s = sys.stdin.readline().split()
    if c == 'insert':
        dic[s] = 0
    else:
        if s in dic:
            print('yes')
        else:
            print('no')