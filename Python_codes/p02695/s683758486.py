import itertools

N, M, Q = map(int, input().split(' '))

q_list = []

for i in range(Q):
    q_list.append(list(map(int, input().split(' '))))


def check(target, point, i):

    if len(q_list) == i:
        return point

    a = q_list[i][0]
    b = q_list[i][1]
    c = q_list[i][2]
    d = q_list[i][3]

    if target[b - 1] - target[a - 1] == c:
        point = check(target, point + d, i + 1)

    else:
        point = check(target, point, i + 1)

    return point


a_list = list(itertools.combinations_with_replacement(range(1, M+1), N))

result = max([check(target, 0, 0) for target in a_list])
print(result)
