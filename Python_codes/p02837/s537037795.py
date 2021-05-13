def main():
    N = int(input())
    A_lst = [0] * N
    xy_lst = [[]] * N
    ans = 0

    for i in range(N):  # 入力
        A = int(input())
        A_lst[i] = A
        xy_lst[i] = [[]] * A

        for j in range(A):
            x, y = map(int, input().split())
            xy_lst[i][j] = [x, y]  # 3次元配列 i人目のj番目の証言の[x,y]

    for i in range(2 ** N):  # ビット全探索
        honest_unkind = [0] * N
        flag = True

        for j in range(N):  # 1つ状態を決める
            if (i >> j) & 1 == 1:
                honest_unkind[j] = 1  # 1:honest, 0:unkind

        for j in range(N):  # 1人ずつ証言を検証する
            if flag == False:
                break

            for k in range(A_lst[j]):  # 各人の証言がk個
                if honest_unkind[j] == 1:  # j番目の人がhonestだったら
                    if xy_lst[j][k][1] == 0 and honest_unkind[xy_lst[j][k][0] - 1] == 1:
                        flag = False  # 矛盾したら終了
                        break
                    if xy_lst[j][k][1] == 1 and honest_unkind[xy_lst[j][k][0] - 1] == 0:
                        flag = False
                        break
                # if honest_unkind[j] == 0:  # j番目の人がunkindだったら
                #     if xy_lst[j][k][1] == 0 and honest_unkind[xy_lst[j][k][0] - 1] == 0:
                #         flag = False
                #         break
                #     if xy_lst[j][k][1] == 1 and honest_unkind[xy_lst[j][k][0] - 1] == 1:
                #         flag = False
                #         break

        if flag == True:  # 全員の証言が矛盾しなかった場合
            cnt = sum(honest_unkind)
            if cnt > ans:
                ans = cnt

    print(ans)


if __name__ == "__main__":
    main()
