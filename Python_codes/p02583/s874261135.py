#!/bin/python3

def main():

    # 変数宣言
    cnt = 0

    # 標準入力からデータの受け取り
    n = int(input())
    l_list = list(map(int, input().split()))
    l_list.sort()

    # 提示条件成立判定＆カウント
    for i in range(0, n - 2):
        for j in range(i + 1, n -1):
            for k in range(j + 1, n):
                if (not((l_list[i] != l_list[j]) and (l_list[i] != l_list[k]) and (l_list[j] != l_list[k]))):
                    continue
                if (not((l_list[i] < l_list[j] + l_list[k]) and (l_list[j] < l_list[i] + l_list[k]) and (l_list[k] < l_list[i] + l_list[j]))):
                    continue
                cnt += 1
    # 結果表示
    print(cnt)


if __name__ == '__main__':
    main()
