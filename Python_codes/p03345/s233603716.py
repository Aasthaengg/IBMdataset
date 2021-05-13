from sys import stdin

a,b,c,k = [int(x) for x in stdin.readline().rstrip().split()]

if k % 2 == 1:
    print(b-a)
else:
    print(a-b)
