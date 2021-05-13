n = int(input())
print(0)
left = input()[0]
if left == 'V':exit()
print(n-1)
right = input()[0]
if right == 'V':exit()

ok = 0
ng = n-1
while ng-ok > 1:
    mid = (ng+ok)//2
    print(mid)
    s = input()[0]
    if s == 'V':exit()
    if mid%2 == 0:
        if s == left:
            ok = mid
        else:
            ng = mid
    else:
        if s != left:
            ok = mid
        else:
            ng = mid