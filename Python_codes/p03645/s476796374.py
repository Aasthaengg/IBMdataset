n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]


def binary_search(num_list, target):
    # 「値が何番目にあるか」を確認するための変数
    ans_counter = 0
    while True:
        # 配列の中心にある値を取り出す
        middle = num_list[len(num_list) // 2]
        # 配列の左側
        left = num_list[:len(num_list) // 2]
        # 配列の右側
        right = num_list[len(num_list) // 2:]
        # 中心の値が探索値と一致したら探索終了(探索値発見)
        if middle == target:
            ans_counter += len(left) + 1
            print("{}は{}番目にありました。".format(target, ans_counter))
            break
        # 値が最後の1個になっても一致しなかったら探索終了(探索値不存在1)
        # 左の最大値 < 探索値 < 右の最小値となった場合探索終了(探索値不存在2)
        elif len(num_list) == 1 and num_list[0] != target\
                or left[-1] < target < right[0]:
            print("{}はありませんでした。".format(target))
            break
        # 左の最大値より探索値が小さい場合、探索範囲を左側に絞る
        elif target <= left[-1]:
            num_list = left
        # 右の最小値より探索値が大きい場合、探索範囲を右側に絞る
        elif right[0] < target:
            ans_counter += len(left)
            num_list = right


first_hune = [False for _ in range(n + 1)]
second_hune = [False for _ in range(n + 1)]

AB.sort(key=lambda x: [x[0], x[1]])
totyu = []
for a, b in AB:
    if a == 1:
        first_hune[b] = True
    if b == n:
        if first_hune[a] is True:
            print('POSSIBLE')
            exit()


print('IMPOSSIBLE')
