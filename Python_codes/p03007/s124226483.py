def c_successive_subtraction(N, A):
    A.sort()
    maximum = A.pop()
    minimum = A.pop(0)

    # Aの要素のうち、最大のものと最小のものを分けて置いておく。
    # それら以外の要素 a_k について、
    # a_k が非負なら、最小のものから a_k を引くことで負の方向に大きくできる。
    # a_k が負なら、最大のものから a_k を引くことで正の方向に大きくできる。
    # 最後に 最大のもの - 最小のもの とすると、最後に残る整数を最大にできる。
    operation = []
    for a in A:
        if a >= 0:
            operation.append('{} {}'.format(minimum, a))
            minimum -= a
        else:
            operation.append('{} {}'.format(maximum, a))
            maximum -= a
    operation.append('{} {}'.format(maximum, minimum))
    return str(maximum - minimum) + '\n' + '\n'.join(operation)

N = int(input())
A = [int(i) for i in input().split()]
print(c_successive_subtraction(N, A))