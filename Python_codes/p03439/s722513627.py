import sys
import math

def get_seat():
    i = input()
    if i == "Vacant":
        sys.exit()
    return i

n = int(input())
print(0)
seat0 = get_seat()

def check_half(s, e):
    half_i = math.floor((e - s) / 2) + s
    if s == e:
        return
    if (s + 1) >= e:
        print(half_i)
        get_seat()
        return
    print(half_i)
    seat = get_seat()
    correct = False
    if (half_i % 2) == 0:
        correct = seat0 == seat
    else:
        correct = seat0 != seat
    if correct:
        # both branches could be correct!
        check_half(half_i + 1, e)
        check_half(s, half_i)
    else:
        # there's a vacant seat at the start
        check_half(s, half_i)

check_half(1, n)
