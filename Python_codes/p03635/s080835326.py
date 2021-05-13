from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 7)
n,m = map(int,stdin.readline().rstrip().split())
print((n-1)*(m-1))