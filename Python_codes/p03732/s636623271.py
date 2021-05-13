

def main():
    num, max_weigh = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(num)]

    data.sort(key=lambda x: (x[0], -x[1]))
    split_data = []

    pre_data = data[0][0]
    pre_ind = 0
    for i in range(num):
        if pre_data != data[i][0]:
            split_data.append(data[pre_ind:i])
            pre_data = data[i][0]
            pre_ind = i
    split_data.append(data[pre_ind:num])

    while len(split_data) != 4:
        split_data.append([])

    ans = 0

    for i in range(-1, len(split_data[0])):
        if i == -1:
            sum_i = 0
            sum_i_w = 0
        else:
            sum_i += split_data[0][i][1]
            sum_i_w += split_data[0][i][0]
        if sum_i_w > max_weigh:
            break
        ans = max(ans, sum_i)

        for j in range(-1, len(split_data[1])):
            if j == -1:
                sum_j = 0
                sum_j_w = 0
            else:
                sum_j += split_data[1][j][1]
                sum_j_w += split_data[1][j][0]
            if sum_i_w + sum_j_w > max_weigh:
                break
            ans = max(ans, sum_i + sum_j)

            for k in range(-1, len(split_data[2])):
                if k == -1:
                    sum_k = 0
                    sum_k_w = 0
                else:
                    sum_k += split_data[2][k][1]
                    sum_k_w += split_data[2][k][0]
                if sum_i_w + sum_j_w + sum_k_w > max_weigh:
                    break
                ans = max(ans, sum_i + sum_j + sum_k)

                for l in range(-1, len(split_data[3])):
                    if l == -1:
                        sum_l = 0
                        sum_l_w = 0
                    else:
                        sum_l += split_data[3][l][1]
                        sum_l_w += split_data[3][l][0]
                    if sum_i_w + sum_j_w + sum_k_w + sum_l_w > max_weigh:
                        break
                    ans = max(ans, sum_i + sum_j + sum_k + sum_l)

    print(ans)



if __name__ == '__main__':
    main()
