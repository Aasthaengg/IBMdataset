def c(N, A):
    A.sort()
    maximum = A.pop()
    minimum = A.pop(0)
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
A = list(map(int, input().split()))
print(c(N, A))