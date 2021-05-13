def matrics_vector_multiply(l1, l2):
    """
    l1: a list(matrics n*m)
    l2: a list(vector  m*1)
    returns a list(vector n*1)

    >>> matrics_vector_multiply([[2]], [0])
    [0]
    >>> matrics_vector_multiply([[1,2,0,1],[0,3,0,1],[4,1,1,0]], [1,2,3,0])
    [5, 6, 9]
    """
    result = []
    for row in l1:
        c = 0
        for i in range(len(row)):
            c += row[i] * l2[i]
        result.append(c)

    return result

if __name__ == '__main__':

    (row, col) = [int(i) for i in input().split(' ')]
    m = []
    v = []
    for r in range(row):
        elms = [int(i) for i in input().split(' ')]
        m.append(elms)
    
    for c in range(col):
        v.append(int(input()))

    for elm in matrics_vector_multiply(m, v):
        print(str(elm))