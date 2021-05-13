import sys

n = int(input())
print(0)
sys.stdout.flush()
ls = input()
if ls == 'Vacant':
    exit()
print(n - 1)
sys.stdout.flush()
if input() == 'Vacant':
    exit()
l = 0
r = n - 1
while l != r - 1:
    mid = (l + r) // 2
    if mid % 2 == 1:
        mid += 1
    if mid == r:
        mid -= 1
    print(mid)
    sys.stdout.flush()
    nex = input()
    if nex == 'Vacant':
        exit()

    if ls == nex:
        l = mid
    else:
        r = mid