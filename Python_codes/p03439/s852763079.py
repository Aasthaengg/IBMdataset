N = int(input())

print(0, flush=True)
begin = input()

l, r = 0, N
while abs(r - l) > 1:
    mid = (l+r) // 2
    print(mid, flush=True)
    sol = input()
    if sol == "Vacant":
        l = mid
        break
    elif mid % 2 == 0:
        if sol != begin:
            r = mid
        else:
            l = mid
    else:
        if sol != begin:
            l = mid
        else:
            r = mid

print(l)
