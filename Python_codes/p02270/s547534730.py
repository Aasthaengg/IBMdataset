def calc_k_constP(P):
    tmp_total_w = 0
    tmp_k = 1
    for w in w_s:
        tmp_total_w += w
        if tmp_total_w > P:
            tmp_k += 1
            tmp_total_w = w

    return tmp_k

n, k = map(int, input().split(' '))
w_s = [int(input()) for i in range(n)]

max_w = max(w_s)

left, right = max_w, 10000 * n
while left < right:
    mid = (right + left) // 2
    tmp_k = calc_k_constP(mid)
    if tmp_k <= k:
        right = mid
    else:
        left = mid + 1

print(left)
