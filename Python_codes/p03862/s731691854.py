def main():
    N, x = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if A[0] > x:
        diff = A[0] - x
        A[0] = x
        ans += diff
    if A[-1] > x:
        diff = A[-1] - x
        A[-1] = x
        ans += diff
    B = [a for a in A]
    ans1 = 0
    for i in range(N-1):
        s = A[i] + A[i + 1]
        if s <= x:
            continue
        diff = s - x
        if diff > A[i + 1]:
            A[i] -= diff - A[i + 1]
            A[i + 1] = 0
        else:
            A[i + 1] -= diff
        ans1 += diff

    ans2 = 0
    for i in range(N - 1):
        index = N - 1 - i
        s = B[index] + B[index - 1]
        if s <= x:
            continue
        diff = s - x
        if diff > B[index - 1]:
            B[index] -= diff - B[index - 1]
            B[index - 1] = 0
        else:
            B[index - 1] -= diff
        ans2 += diff
    ans += min(ans1, ans2)

    print(ans)

if __name__ == '__main__':
    main()
