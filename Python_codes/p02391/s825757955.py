import sys

a,b = map(int, sys.stdin.readline().rstrip().split(' '))
mark = '==' if (a==b) else '>' if (a>b) else '<'
print("a {} b".format(mark))