
def resolve():
    N = int(input())
    A = sorted(map(int, input().split()))

    idx = 0
    tmp = 0
    for i in range(N):
        if tmp * 2 < A[i]:
            idx = i
        tmp += A[i]

    print(N - idx)


if __name__ == "__main__":
    resolve()