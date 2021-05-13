def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split(' ')))
    # 対称性から、左半分（中央含む）の各場所でのアサイン候補人数だけ考える。
    # 中央では1人、その他では2人（左右それぞれにアサイン）であればOK。
    # アサイン可能なのであれば答えは 2 ** (N // 2) 通り。
    count = [0 for _ in range(N // 2 + 1)]
    for a in A:
        if (N - 1 - a) % 2 > 0:
            print(0)
            return
        left = (N - 1 - a) // 2  # right = (N - 1 + a) // 2
        count[left] += 1
    for i in range(len(count)):
        c = count[i]

        if i == N // 2:
            if N % 2 > 0 and c != 1:
                print(0)
                return
        else:
            if c != 2:
                print(0)
                return
    # caclulate answer
    ans = 1
    for _ in range(N // 2):
        ans *= 2
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()