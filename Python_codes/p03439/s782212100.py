n = int(input())

print(0, flush=True)
res = input()
if res == "Vacant":
    exit()

left = 0
right = n
gen = res


while True:
    mid = (left + right) // 2
    print(mid, flush=True)
    res = input()

    if res == "Vacant":
        exit()

    if gen == res:
        if (mid - left) % 2:
            right = mid
        else:
            left = mid
    else:
        if (mid - left) % 2:
            left = mid
            gen = res
        else:
            right = mid