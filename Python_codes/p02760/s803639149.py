def check(A):
    """ check bingo or not
    :param A: 3*3 matrix, 1 or 0
    :return: is_bingo bool
    """
    for row_id in range(3):
        if sum(A[row_id])==3:
            return True
    
    for column_id in range(3):
        column_sum = 0
        for row_id in range(3):
            column_sum += A[row_id][column_id]
        if column_sum == 3:
            return True

    lr_sum = 0
    rl_sum = 0
    for rc_id in range(3):
        lr_sum += A[rc_id][rc_id]
        rl_sum += A[rc_id][2-rc_id]
    if lr_sum == 3 or rl_sum == 3:
        return True
        
    return False


def search(query, A):
    for row_id in range(3):
        for column_id in range(3):
            if query == A[row_id][column_id]:
                return column_id, row_id 
    return None, None


if __name__ == '__main__':
    A = [list(map(int, input().split())) for _ in range(3)]
    B = [[0, 0, 0] for _ in range(3)]

    N = int(input())

    for _ in range(N):
        query = int(input())
        i, j = search(query, A)
        if i != None and j != None:
            B[i][j] = 1

    if check(B):
        print('Yes')
    else:
        print('No')
