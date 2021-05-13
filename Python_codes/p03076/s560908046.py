import itertools


def actual(a, b, c, d, e):
    all_permutations = list(itertools.permutations([a, b, c, d, e], 5))

    order_time_list = []

    for orders in all_permutations:
        elapsed_time = 0

        for i in range(5):
            elapsed_time += orders[i]

            if i == 4:
                # 最後の注文は時間の調整不要
                continue

            fraction = elapsed_time % 10

            if fraction != 0:
                # 10で割り切れない場合は注文できないのでそれを調整する
                # ex: 57分なら +3分(⇔10 - 57%10)
                elapsed_time += 10 - fraction

        order_time_list.append(elapsed_time)

    return min(order_time_list)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(actual(a, b, c, d, e))