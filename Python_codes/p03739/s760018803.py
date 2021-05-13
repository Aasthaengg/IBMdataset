from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))


def func(a, judge):
    sum_list = list(accumulate(a))
    x = 0
    num = 0

    length = len(sum_list)

    for i in range(length):
        if judge and sum_list[i] + x <= 0:
            num += 1 - (sum_list[i] + x)
            x += 1 - (sum_list[i] + x)

        if (not judge) and sum_list[i] + x >= 0:
            num += 1 + (sum_list[i] + x)
            x -= 1 + (sum_list[i] + x)

        judge = not judge

    return num


ans = min([func(A, True), func(A, False)])

print(ans)
