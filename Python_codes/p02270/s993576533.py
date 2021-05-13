#coding:utf-8
#1_4_D
def is_carriable(w_lim, trucks, loads):
    """ Check whether w_lim(maximum carrying capacity) is possible or not """
    i = 0
    while trucks > 0:
        w = 0
        while i < len(loads):
            if w + loads[i] > w_lim:
                trucks -= 1
                break
            w += loads[i]
            i += 1
        if i == len(loads):
            return True
    return False

n, trucks = map(int, input().split())
loads = [int(input()) for i in range(n)]

left = max(loads)
right = sum(loads) + 1

while right - left > 1:
    mid = (left + right) // 2
    if is_carriable(mid, trucks, loads):
        ans = mid
        right = mid
    else:
        left = mid

if is_carriable(max(loads), trucks, loads):
    ans = max(loads)

print(ans)