import sys
input=sys.stdin.readline
N=int(input())
m=[]
a=[-float("inf"), float("inf")]
b=[-float("inf"), float("inf")]
for _ in range(N):
    x, y = map(int, input().split())
    a[0] = max(a[0], x+y)
    a[1] = min(a[1], x+y)
    b[0] = max(b[0], x-y)
    b[1] = min(b[1], x-y)
print(max(abs(a[0]-a[1]), abs(b[0]-b[1])))
