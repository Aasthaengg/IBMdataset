def color(s):
    col = 'black'
    if s == '.':
        col = 'white'
    return col


def main():
    h, w = map(int, input().split())
    s_lst = list(str(input()) for _ in range(h))
    sw_lst = []
    for i in range(h):
        tmp_lst = []
        s = s_lst[i]
        for j in range(w):
            tmp_lst.append(s[j])
        sw_lst.append(tmp_lst)

    flag = True
    black_count = 0

    for i in range(h):
        for j in range(w):

            surroundings = []
            if color(sw_lst[i][j]) == 'black':
                black_count += 1
                if i != 0:
                    surroundings.append(color(sw_lst[i - 1][j]))
                if i != h - 1:
                    surroundings.append(color(sw_lst[i + 1][j]))
                if j != 0:
                    surroundings.append(color(sw_lst[i][j - 1]))
                if j != w - 1:
                    surroundings.append(color(sw_lst[i][j + 1]))

                if 'black' not in surroundings:
                    flag = False

    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()