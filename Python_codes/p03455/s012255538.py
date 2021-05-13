from sys import stdin
a,b = [int(x) for x in stdin.readline().rstrip().split()]

x = a*b

if x % 2 == 1:
    print('Odd')
else:
    print('Even')