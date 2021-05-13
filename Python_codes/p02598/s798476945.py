import heapq
n , k = map(int,input().split())
a = list(map(int,input().split()))
lef = 0
rig = max(a)
while rig - lef != 1:
    now = -(-(lef+rig)//2)
    cou = 0
    for i in range(n):
        cou += -(-a[i]//now) - 1
    if cou <= k:
        rig = now
    elif cou > k:
        lef = now
print(rig)