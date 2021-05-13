import sys
input = sys.stdin.readline
n,T = map(int,input().split())
t = list(map(int,input().split()))
h = 0
for i in range(1,n):
    if t[i] - t[i-1] < T:
        h += T - (t[i] - t[i-1])
print(T*n - h)
