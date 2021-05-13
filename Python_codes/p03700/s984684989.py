import sys
input = sys.stdin.readline
n,a,b = map(int,input().split())
h = [int(input()) for i in range(n)]
t = a-b
r = (max(h)+b-1)//b
l = 0
while r-l > 1:
    m = (r+l)//2
    mi = m*b
    count = 0
    for i in h:
        if i > mi:
            count += (i-mi+t-1)//t
    if count <= m:
        r = m
    else:
        l = m
print(r)