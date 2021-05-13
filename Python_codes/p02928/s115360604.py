N, K = map(int, input().split())
A_list = list(map(int, input().split()))

K_seq_sum1 = K*(K+1)//2
K_seq_sum2 = K*(K-1)//2
# print(K_seq_sum)
# その中での転倒数と
# 自分より低い数を持っておく
inv_num_in_original_list = []
inv_num_all_list = []
diff_lst = []
res = 0
for n1, a1 in enumerate(A_list):
    cnt1 = 0
    cnt2 = 0
    for n2, a2 in enumerate(A_list):
        if a1 > a2:
            cnt2 += 1
            if n1 < n2:
                cnt1 += 1
    diff = cnt2 - cnt1
    # a1から見たときの数を出す
    # (自分のリストの中での転倒の数 * K回) + (自分より左のリストとの転倒数)
    # res_tmp = cnt1 * K + cnt2 * K_seq_sum
    # res += res_tmp s
    res_tmp = diff * K_seq_sum2 + cnt1 * K_seq_sum1
    res += res_tmp
    res = int(res % (10**9+7))
print(res)

