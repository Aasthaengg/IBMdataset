def main():
    N, K = map(int, input().split())
    A = [int(a) for a in input().split()]

    B0 = ans = 0

    for i in range(len(A) - 1):
        count = 0
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                B0 += 1

    ans += (B0 * K)

    for i in range(len(A)):
        count = 0
        for j in range(len(A)):
            if A[i] > A[j]:
                count += 1
        
        ans += (count * (K - 1) * K // 2)

    print(ans % (10**9 + 7))

if __name__ == "__main__":
    main()