from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)


def judge(x):
    y = k
    for i in range(n):
        goal = x//f[i]
        if a[i] > goal:
            y -= a[i] - goal
            if y < 0:
                return False
    return y >= 0


left = -1
right = 10**12 + 1
while left + 1 < right:
    mid = (left + right)//2
    if judge(mid):
        right = mid
    else:
        left = mid

print(right)
