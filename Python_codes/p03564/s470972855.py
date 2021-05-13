def actual(N, K):
    # 2つの操作のうち、小さくなる方を選び続ければよい
    op_A = lambda i: i * 2
    op_B = lambda i: i + K

    num = 1

    for _ in range(N):
        num = min(op_A(num), op_B(num))

    return num

N = int(input())
K = int(input())
print(actual(N, K))