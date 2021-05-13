def main():

    # 割引時の最小値と個別購入の最小値を比較する必要あり

    a_num, b_num, m = map(int, input().split())

    a_val = list(map(int, input().split()))
    b_val = list(map(int, input().split()))

    values = []
    for i in range(m):
        values.append(list(map(int, input().split())))

    set_value = []
    for i in range(len(values)):
        set_value.append(a_val[values[i][0]-1] +
                         b_val[values[i][1]-1] - values[i][2])
    min_set_value = min(set_value)

    solo_value = min(a_val) + min(b_val)

    answer = min_set_value if min_set_value <= solo_value else solo_value

    print(answer)


if __name__ == "__main__":
    main()
