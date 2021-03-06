import math


def check(m, A, V):
    # whether we can get `m` for mean of values
    cnt, x = 0, 0
    for v in V[:A]:
        x += v - m
        cnt += 1
    return x >= 0


def comb(n, k):
    if k > n - k:
        return comb(n, n - k)
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


def main():
    N, A, B = list(map(int, input().split(' ')))
    V = list(map(int, input().split(' ')))
    V.sort(reverse=True)
    # calculate max average value by binary search
    eps = 10 ** (-15)
    ok, ng = 0, 10 ** 16
    while (ng - ok) / ng > eps:
        mid = (ok + ng) / 2
        if check(mid, A, V):
            ok = mid
        else:
            ng = mid
    ans_v = ok
    # calculate pattern number
    min_target_v = V[A - 1]
    target_v_cnt = sum([1 if v == min_target_v else 0 for v in V])
    selected_target_v_cnt = sum([1 if v == min_target_v else 0 for v in V[:A]])
    ans_pattern = comb(target_v_cnt, selected_target_v_cnt)
    if V[0] == min_target_v:  # V[0] == ... == V[A - 1]
        # the average does not change if we add another item with min_target_v
        for i in range(1, B - A + 1):
            if target_v_cnt < selected_target_v_cnt + i:
                break
            ans_pattern += comb(target_v_cnt, selected_target_v_cnt + i)
    # answer
    print(ans_v)
    print(ans_pattern)


if __name__ == '__main__':
    main()