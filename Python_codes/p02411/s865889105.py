def get_perfomance(score):
    m, f, r = score
    sum_mf = m + f
    if 0 > m or 0 > f:
        return 'F'
    elif 80 <= sum_mf:
        return 'A'
    elif 65 <= sum_mf:
        return 'B'
    elif 50 <= sum_mf:
        return 'C'
    elif 30 <= sum_mf:
        if 50 <= r:
            return 'C'
        else:
            return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    score_list = []
    while True:
        values = [int(x) for x in input().split()]
        if 3 == values.count(-1):
            break
        score_list.append(values)

    for score in score_list:
        print(get_perfomance(score))