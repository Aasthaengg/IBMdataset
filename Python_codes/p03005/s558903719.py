from sys import stdin
l = stdin.readline().rstrip().split()

n = int(l[0])
k=int(l[1])

if k == 1:
    print(0)
else:
    print(n-k)