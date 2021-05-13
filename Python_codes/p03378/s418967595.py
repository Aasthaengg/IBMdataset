def actual(N, M, X, A):
    # マスXの左右それぞれにある料金所の数を調べればOK
    toll_gates_left = [a_i for a_i in A if a_i < X]
    toll_gates_right = [a_i for a_i in A if X < a_i]

    return min(len(toll_gates_left), len(toll_gates_right))

N, M, X = map(int, input().split())
A = list(map(int, input().split()))

print(actual(N, M, X, A))
