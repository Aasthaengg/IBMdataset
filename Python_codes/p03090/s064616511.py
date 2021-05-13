
def find(n):
    """
    tn = int(n/2)
    s = 2 * tn + 1
    :param n:
    :return:
    """
    tn = int(n / 2)
    s = 2 * tn + 1
    count = 0
    line_list = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i + j != s:
                line_list.append(str(i) + " " + str(j))
                count += 1

    return count, line_list


if __name__ == '__main__':
    n = int(input())

    count, line_list = find(n)
    print(count)
    for item in line_list:
        print(item)