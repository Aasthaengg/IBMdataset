import sys
input = sys.stdin.readline

N = int(input())
left = 0
right = N
print(left, flush=True)
left_seat = input()
if left_seat == 'Vacant':
    exit()


while right - left > 1:
    mid = (left + right) // 2
    print(mid, flush=True)
    mid_seat = input()
    if mid_seat == 'Vacant':
        exit()
    if mid_seat == left_seat:
        if (mid - left) % 2 == 0:
            left = mid
        else:
            right = mid
    else:
        if (mid - left) % 2 == 1:
            left = mid
            left_seat = mid_seat
        else:
            right = mid
