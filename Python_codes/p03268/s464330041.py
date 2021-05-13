N, K = map(int, input().split())

if K % 2 != 0:
    ans_odd = []
    for i in range(N):
        if ((i + 1) % K) == 0:
            ans_odd.append(i + 1)

    len_ans = len(ans_odd)
    print(len_ans * len_ans * len_ans)

else:
    ans_even_zero = []
    ans_even_k = []
    for i in range(N):
        if (i + 1) % K == 0:
            ans_even_zero.append(i + 1)
        elif (i + 1) % K == (K // 2):
            ans_even_k.append(i + 1)

    len_ans_even_zero = len(ans_even_zero)
    len_ans_even_k = len(ans_even_k)

    ans = len_ans_even_zero * len_ans_even_zero * \
        len_ans_even_zero + len_ans_even_k * len_ans_even_k * len_ans_even_k
    print(ans)
