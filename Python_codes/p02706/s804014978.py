
if __name__ == '__main__':
    """
    :param N: days
    :param M: num of homeworks
    :param A: days to finish each homework
    """
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    need = sum(A)
    if N >= need:
        print(N-need)
    else:
        print(-1)

