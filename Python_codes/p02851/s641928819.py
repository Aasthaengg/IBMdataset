def e_rem_of_sum_is_num():
    # 参考: https://maspypy.com/atcoder-参加感想-2019-11-16abc-146
    from itertools import accumulate
    from collections import defaultdict

    N, K = [int(i) for i in input().split()]
    # 1 引くと、条件を満たす連続部分列の要素の平均は 0 (mod K で) となる
    A = [0] + [int(i) - 1 for i in input().split()]

    acc = list(accumulate(A))
    acc = [x % K for x in acc]  # mod K 上で同一視する

    # S_j ≡ S_i となるような j-K < i < j の個数を数え上げればいい。
    # そのためには、j 未満のインデックスに対する S の度数分布を管理しておけばいい。
    counter = defaultdict(int)  # 値の度数分布
    ans = 0
    for j, x in enumerate(acc):
        ans += counter[x]
        # 数列の右端を追加
        counter[x] += 1
        # 数列の左端を削除 (数列の長さが K 未満になるようにする。
        # 数列の長さが K 以上だと、数列の和を K で割った余りと一致するはずがない)
        if j - K + 1 >= 0:
            counter[acc[j - K + 1]] -= 1
    return ans

print(e_rem_of_sum_is_num())