from sys import stdin,setrecursionlimit
import string
setrecursionlimit(10 ** 7)
n = int(stdin.readline().rstrip())
print(n*(n-1)//2)