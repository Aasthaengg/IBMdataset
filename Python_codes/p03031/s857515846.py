def main():
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    ans = 0

    for i in range(2 ** N):  # スイッチの状態をビット全探索
        switch = [0] * N
        flag = True

        for j in range(N):  # スイッチの状態を1パターン決める 1:ON, 0:OFF
            if ((i >> j) & 1):
                switch[j] = 1

        for j in range(M):  # 各電球について条件を満たすか確認
            cnt = 0  # 各電球についてonになっているスイッチの数
            for k in lst[j][1:]:
                if switch[k - 1] == 1:
                    cnt += 1

            if cnt % 2 != p[j]:  # 1つでも点灯しない電球があったら現在のスイッチの状態はだめ
                flag = False
                break

        if flag == True:  # すべての電球が点灯する
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
