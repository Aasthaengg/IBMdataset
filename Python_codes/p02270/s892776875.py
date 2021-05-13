def check(w_list, k, P):
    tmp = 0
    tmp_k = 1
    if max(w_list) > P:
        return False
    for w in w_list:
        tmp += w
        if tmp > P:
            tmp_k += 1
            tmp = w
    if tmp_k <= k:
        return True
    else:
        return False


def binary_search(w_list, k, l, r):
    while(r - l > 1):
        c = (l + r) // 2
        # print(c)
        # print(check(w_list, k, c))
        if check(w_list, k, c):
            r = c
        else:
            l = c

    return r


n, k = map(int, input().split())
w_list = []
for _ in range(n):
    w_list.append(int(input()))

max_P = n * 10000

min_P = binary_search(w_list, k, 0, max_P)

print(min_P)

