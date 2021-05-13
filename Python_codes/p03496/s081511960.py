def d_non_decreasing(N, A):
    a_max = max(A)
    a_argmax = A.index(a_max) + 1
    a_min = min(A)
    a_argmin = A.index(a_min) + 1  # +1するのは問題の数列が1-indexedだから

    if abs(a_max) >= abs(a_min):
        plus_index = a_argmax
        cumsum_range = range(1, N)
        cumsum_direction = +1
    else:
        plus_index = a_argmin
        cumsum_range = range(N, 1, -1)
        cumsum_direction = -1

    ans = [str(2 * N - 1)]  # 2N-1回の操作でソートされた数列になる
    for k in range(1, N + 1):
        ans.append('{} {}'.format(plus_index, k))  # 各要素に一律に加算
    for k in cumsum_range:
        ans.append('{} {}'.format(k, k + cumsum_direction))  # 累積和を取る
    ans = '\n'.join(ans)
    return ans
  
N = int(input())
A = [int(i) for i in input().split()]
print(d_non_decreasing(N, A))