
ans_data = []

def get_num_shugou(num):
    num_shuugou = -1
    for i in range(1, num + 2):
        if 2 * num == i * (i - 1):
            num_shuugou = i
            break
        elif 2 * num < i * (i - 1):
            break
    return num_shuugou

def get_piramid(num_shuugou):
    piramid = [[1]]
    for i in range(num_shuugou - 2):
        data = [piramid[-1][-1] + j + 1 for j in range(len(piramid) + 1)]
        piramid.append(data)
    return piramid


def data_append(now_list):
    print('{} {}'.format(len(now_list), ' '.join(list(map(str, now_list)))))


def make_data(high, width, piramid, now_list_kari, down_flg):
    now_list = now_list_kari.copy()
    now_list.append(piramid[high][width])

    if len(now_list) == len(piramid):
        data_append(now_list)
        return

    if down_flg:
        make_data(high + 1, width, piramid, now_list, down_flg)

    elif width == len(piramid[high]) - 1:
        down_flg = 1
        make_data(high + 1, width, piramid, now_list, down_flg)
    else:
        make_data(high, width + 1, piramid, now_list, down_flg)


def write_shugou(num_shuugou):
    piramid = get_piramid(num_shuugou)

    now_list = [piramid[i][-1] for i in range(len(piramid))]
    data_append(now_list)
    for i in range(num_shuugou - 1):
        make_data(i, 0, piramid, [], 0)

def main():
    num = int(input())
    num_shuugou = get_num_shugou(num)
    if num_shuugou == -1:
        print('No')
    else:
        print('Yes')
        print(num_shuugou)
        write_shugou(num_shuugou)



if __name__ == '__main__':
    main()