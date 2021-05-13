# AOJ 0003 Is it a Right Triangle?
# Python3 2018.6.7 bal4u

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    if a[0]*a[0] + a[1]*a[1] == a[2]*a[2]:
        print('YES')
    else:
        print('NO')
