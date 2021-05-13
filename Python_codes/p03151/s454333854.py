def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    res = 0
    if sum(A) < sum(B):
        print(-1)
        exit()

    # まず不足している準備度を求める
    # また、余ってたら余ってる量をCにブチこんでいく
    C = list()
    missing = 0
    ans = 0
    for i in range(N):
        if A[i] < B[i]:
            missing += (B[i] - A[i])
            ans += 1
        else:
            C.append(A[i]-B[i])

    if missing == 0:
        print(0)
        exit()

    C.sort(reverse=True)

    for c in C:
        if missing <= c:
            ans += 1
            break
        else:
            missing -= c
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
