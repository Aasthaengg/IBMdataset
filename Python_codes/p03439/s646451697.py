N = int(input())

li = 0
print(li, flush=True)
ls = input()
if ls == 'Vacant':
    exit()

ri = N - 1
print(ri, flush=True)
rs = input()
if rs == 'Vacant':
    exit()

for _ in range(18):
    mid = (li + ri) // 2

    print(mid, flush=True)
    s = input()

    if s == 'Vacant':
        exit()

    # [li, mid]に空席がある
    c1 = (mid - li) % 2 == 1 and ls == s
    c2 = (mid - li) % 2 == 0 and ls != s
    if c1 or c2:
        ri = mid
        rs = s
    else:
        li = mid
        ls = s