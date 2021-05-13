n = int(input())

left = 0
right = n
print(left, flush=True)
sl = input()
if sl[0] == "V":
    quit()
while right - left > 1:
    mid = (left + right) // 2
    print(mid, flush=True)
    sm = input()
    if sm[0] == "V":
        quit()

    if ((mid - left) % 2 == 1) ^ (sl == sm):
        left = mid
        sl = sm
    else:
        right = mid

