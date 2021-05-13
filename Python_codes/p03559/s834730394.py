import bisect

def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    # print(N, A, B, C)
    # print(A)
    # print(B)
    # print(C)
    B1 = [0]*N
    for i in range(N):
        b = B[i]
        B1[i] = N - bisect.bisect_right(C, b)
        if i != 0:
            B1[i] += B1[i - 1]
    A1 = [0]*N
    for i in range(N):
        a = A[i]
        index = bisect.bisect_right(B, a)
        if index == 0:
            A1[i] = B1[-1]
        elif index < N:
            A1[i] = B1[-1] - B1[index - 1]
    ans = sum(A1)
    # print(B1, A1)
    print(ans)

if __name__ == '__main__':
    main()
