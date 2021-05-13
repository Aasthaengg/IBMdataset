import sys

a,b,c = map(str,sys.stdin.readline().rstrip())
d,e,f = map(str,sys.stdin.readline().rstrip())
print('YES' if a == f and b == e and c == d else 'NO')
