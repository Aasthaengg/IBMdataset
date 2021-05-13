
N = int(input())

print(0, flush=True)
S = input()
if S == "Vacant":
    exit()
lo = 0
hi = N
while hi - lo > 1:
    mid = (hi + lo) // 2
    print(mid, flush=True)
    tmp = input()
    if tmp == "Vacant":
        exit()
    else:
        if mid % 2 == 0:
            if tmp == S:
                lo = mid
            else:
                hi = mid
        else:
            if tmp != S:
                lo = mid
            else:
                hi = mid
