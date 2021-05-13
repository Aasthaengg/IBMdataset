N = int(input())
A = list(map(int, input().split()))
M_DICT = {}


def make_m(i, m):
    if (i, m) in M_DICT:
        return M_DICT[(i, m)]
    if m == 0:
        return True
    if i >= N or m < 0:
        return False

    res = make_m(i+1, m) or make_m(i+1, m-A[i])
    M_DICT[(i, m)] = res
    return res


def main():
    q = int(input())
    m_lst = list(map(int, input().split()))

    for i in range(q):
        if make_m(0, m_lst[i]):
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    main()

