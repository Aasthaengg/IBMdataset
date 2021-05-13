def main(A, B, C, K):
    """
    a = [1 for _ in range(A)]
    b = [0 for _ in range(B)]
    c = [-1 for _ in range(C)]
    k = a + b + c
    ans = sum(k[:K])
    """
    if K <= A:
        return K
    if A <= K <= A+B:
        return A
    else:
        return A - (K-A-B)

if __name__ == '__main__':
    A, B, C, K = map(int, input().split())
    ans = main(A, B, C, K)
    print(ans)

