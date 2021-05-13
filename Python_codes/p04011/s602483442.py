import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
k = int(input())
x = int(input())
y = int(input())

temp = min([n,k]) * x
if k<n:
    temp += (n-k) * y
print(temp)