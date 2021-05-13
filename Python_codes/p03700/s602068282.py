import sys
input = sys.stdin.readline

n, a, b = [int(x) for x in input().split()]
h = [int(input()) for _ in range(n)]

left = 0
right = 10**10

def solve(x):
    remain = []
    for i in h:
        i -= b*x
        if i > 0:
            remain.append(i)
    cnt = 0
    for i in remain:
        cnt += i // (a - b) + int(i % (a - b) != 0)
    if cnt <= x:
        return True
    else:
        return False

while right - left > 1:
    mid = (right + left) // 2
    if solve(mid):
        right = mid
    else:
        left = mid

print(right)




