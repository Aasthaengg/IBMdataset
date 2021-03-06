import math


def calc_minkowski_distance(data_x, data_y, types):
    # ???????´???????????¨???????map???????????¬??????????????????????????¨????????¨????????§?¶???????????????????????????§????????????????????????
    distance = list(map(lambda x, y:abs(x - y), data_x, data_y))

    results = []
    for t in types:
        if t == 'Inf':
            results.append(max(distance))
        else:
            temp = map(lambda x:math.pow(x, t), distance)
            total = sum(temp)
            results.append(math.pow(total, 1.0/t))
    return results


if __name__ == '__main__':
    # ??????????????\???
    # data_x = [1, 2, 3]
    # data_y = [2, 0, 4]
    num = int(input())
    data_x = [int(x) for x in input().split(' ')]
    data_y = [int(x) for x in input().split(' ')]

    # ???????????????
    types = [1, 2, 3, 'Inf']  # math.inf???python3.5??\?????????
    results = calc_minkowski_distance(data_x, data_y, types)

    # ???????????¨???
    for r in results:
        print('{0:.8f}'.format(r))