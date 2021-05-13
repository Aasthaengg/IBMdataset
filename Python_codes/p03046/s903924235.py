def f_xor_matching(M, K):
    if K >= 2**M:
        return -1

    if M == 0:
        ans = [0, 0]
    elif M == 1:
        ans = [0, 0, 1, 1] if K == 0 else [-1]
    else:
        b = [k for k in range(2**M) if k != K]
        ans = b + [K] + b[::-1] + [K]
    return ' '.join(map(str, ans))

M, K = [int(i) for i in input().split()]
print(f_xor_matching(M, K))