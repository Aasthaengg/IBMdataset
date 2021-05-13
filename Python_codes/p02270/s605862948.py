import sys

def check_sekisairyo(p_min):
    p_now = 0
    k_now = 0
    for w in w_i:
        p_now += w
        if p_now > p_min:
            p_now = w
            k_now += 1
        elif p_now == p_min:
            p_now = 0
            k_now += 1
        if k_now == k and p_now != 0:
            return False
    return True

n, k = map(int, input().split())
w_i = [int(input()) for i in range(n)]
left, right, p_min = max(w_i), sum(w_i), 0
while left < right:
    p_min = (left + right) // 2
    if check_sekisairyo(p_min):
        right = p_min
    else:
        left = p_min = p_min + 1
print(p_min)