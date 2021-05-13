import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
l = 0
r = int(1e9)

def f(x):
    count = 0
    for a in A:
        count += int((a-1)/x)
    return count <= K

while r-l > 1:
    x = int((r+l)/2)
    if f(x):
        r = x
    else:
        l = x
print(r)