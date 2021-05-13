N = int(input())
print(0, flush=True)
s = input()
if s == 'Vacant':
    exit()
l, r = 0, N
while True:
    mid = (l + r) // 2
    print(mid, flush=True)
    t = input()
    if s == 'Vacant':
        break
    # 時計回りに席を埋めていくと奇数席で0と性別が異なる
    if mid % 2:
        if s != t:
            l = mid
        else:
            r = mid
    else:
        if s == t:
            l = mid
        else:
            r = mid