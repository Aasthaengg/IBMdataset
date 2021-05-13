n, m = map(int, input().split())
l1 = []
ln = []
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        l1.append(b)
    elif b == 1:
        l1.append(a)
    elif a == n:
        ln.append(b)
    elif b == n:
        ln.append(a)
l1.sort()
ln.sort()
ans = False
for i in l1:
    low = 0
    high = len(ln) - 1
    while low <= high:
        mid = (low + high)//2
        if ln[mid] == i:
            ans = True
            break
        elif ln[mid] > i:
            high = mid - 1
        else:
            low = mid + 1
    if ans:
        break
if ans:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")