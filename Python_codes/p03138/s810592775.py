def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = bin(K)[2:]
    B = B[::-1]
    BB = len(bin(10 ** 12)) - 2
    T = [0] * BB
    for i in range(BB):
        T[i] = sum((a & (1 << i)) >> i for a in A)
    if K == 0:
        print(sum(A))
        return
    m = 0
    def h(i, f):
        if i < 0:
            return 0
        if i >= len(B):
            return (T[i] << i) + h(i - 1, False)
        if f:
            return (max(T[i], N - T[i]) << i) + h(i - 1, f)
        if B[i] == '0':
            return (T[i] << i) + h(i - 1, False)
        return max((T[i] << i) + h(i - 1, True), ((N - T[i]) << i) + h(i - 1, False))
    print(h(BB - 1, False))

main()
