def solve():


    A, B, C, D, E, F = map(int, input().split())

    #memo
    list = {}

    #操作1-4
    ope1 = 100 * A
    ope2 = 100 * B
    ope3 = C
    ope4 = D


    for i in range(31):
        for j in range(31):
            for k in range(101):
                for l in range(101):
                    w_sum = i * ope1 + j * ope2
                    s_sum = k * ope3 + l * ope4
                    if w_sum == 0:
                        break
                    if w_sum+s_sum > F:
                        break
                    else:
                        if w_sum/100 * E >= s_sum:
                            p_tmp = (s_sum / (w_sum + s_sum)) * 100
                            list[i, j, k, l] = p_tmp

    max_v = max(list.values())

    for k, v in list.items():
        if v == max_v:
            print(ope1*k[0] + ope2*k[1] + ope3*k[2] + ope4*k[3], ope3*k[2] + ope4*k[3])
            break

if __name__ == "__main__":
    solve()
