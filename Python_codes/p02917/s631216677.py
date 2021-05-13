def main(N, B):
    A = [-1 for _ in range(N)]
    A[0], A[-1] = B[0], B[-1]

    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])

    return(sum(A))


if __name__ == "__main__":
    N = int(input())
    B = list(map(int, input().split()))
    ans = main(N, B)
    print(ans)
