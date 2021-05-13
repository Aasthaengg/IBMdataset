import sys

def input():
    return sys.stdin.readline()[:-1]


n, k = map(int, input().split())
a_li = list(map(int, input().split()))

if k>=42:
    print(*[n]*n)
    exit()

for i in range(k):
    b = [0] * n
    for j in range(n):
        l = max(0, j-a_li[j])
        r = min(n-1, j+a_li[j])
        b[l] += 1
        if (r+1<n):
            b[r+1] -= 1
    for j in range(n-1):
        b[j+1] += b[j]
    a_li = b
print(*a_li)