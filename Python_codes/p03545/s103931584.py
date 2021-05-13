def operator(x):
    if x < 0:
        return '-'
    else:
        return '+'


def main():
    abcd = str(input())
    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])

    lst = []
    for op_1 in range(2):
            for op_2 in range(2):
                for op_3 in range(2):

                    b1 = b
                    c1 = c
                    d1 = d
                    if op_1 == 1:
                        b1 = -b
                    if op_2 == 1:
                        c1 = -c
                    if op_3 == 1:
                        d1 = -d

                    if b1 + c1 + d1 == 7 - a:
                        lst.append(b1)
                        lst.append(c1)
                        lst.append(d1)
                        break

    op1 = operator(lst[0])
    op2 = operator(lst[1])
    op3 = operator(lst[2])
    answer = str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + '=' + '7'
    print(answer)


if __name__ == '__main__':
    main()