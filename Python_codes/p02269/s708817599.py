import sys

n = int(input())
dic = set()
for i in range(n):
    s = sys.stdin.readline()
    if s[0] == "i":
        dic.add(s[7:])
    else:
        print('yes' if s[5:] in dic else 'no')