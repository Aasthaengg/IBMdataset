def p_d():
    n, k = map(int, input().split())
    *A, = map(int, input().split())
    size = (len(bin(max(A + [k]))) - 2)
    bits = [0] * size
    for a in A:
        for i in range(len(bin(a)) - 2):
            bits[i] += a >> i & 1

    now = 0
    ans = 0
    for i, bit_count in enumerate(reversed(bits)):
        b = 1 << size - i - 1
        if k < now | b or n - bit_count <= bit_count:
            ans += bit_count * b
            continue
        now |= b
        ans += (n - bit_count) * b

    print(ans)


if __name__ == '__main__':
    p_d()
