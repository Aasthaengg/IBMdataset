def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(N, A, B)
    expected = sum(B) - sum(A)
    if expected < 0:
        print('No')
        return
    add_a, add_b = 0, 0
    for i in range(N):
        a, b = A[i], B[i]
        if a > b:
            add_b += a - b
        elif a < b:
            add_a += (b - a + 1) // 2
    if add_a <= expected and add_b <= expected:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
