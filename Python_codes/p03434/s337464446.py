import sys
n,*a=map(int,sys.stdin.read().split())
a.sort(reverse=True)
print(sum(a[::2])-sum(a[1::2]))