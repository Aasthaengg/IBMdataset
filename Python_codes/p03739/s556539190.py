n = int(input())
a_list = list(map(int, input().split()))

sum1 = a_list[0]

def func(sum1):
    cost = 0
    for i in a_list[1:]:
        # 前の合計値と次の合計値の積が負になれば良い
        if sum1 * (sum1 + i) < 0:
            sum1 += i
            continue
        else:
            if sum1 < 0:
                a_new = 1 - sum1
                cost += a_new - i
                sum1 += a_new
            else:
                a_new = -1 - sum1
                cost += i - a_new
                sum1 += a_new

    return cost

if a_list[0] > 0:
    # リストの最初が-1の場合のコストも考える
    answer = min(func(sum1), func(-1)+a_list[0]+1)
elif a_list[0] < 0:
    answer = min(func(sum1), func(1)-a_list[0]+1)
else:
    # リストの最初が0だったとき
    answer = min(func(1), func(-1)) + 1

print(answer)