import math

n = int(input())

def foo(p1, p2):
    s_x = p1[0] + (p2[0] - p1[0]) / 3.0
    s_y = p1[1] + (p2[1] - p1[1]) / 3.0
    t_x = p1[0] + (2 * (p2[0] - p1[0])) / 3.0
    t_y = p1[1] +  (2 * (p2[1] - p1[1])) / 3.0
    u_x = math.cos(math.radians(60)) * (t_x - s_x) - math.sin(math.radians(60)) * (t_y - s_y) + s_x
    u_y = math.sin(math.radians(60)) * (t_x - s_x) + math.cos(math.radians(60)) * (t_y - s_y) + s_y

    return [[s_x, s_y], [u_x, u_y], [t_x, t_y]]

def bar(arr):
    result = []
    for i in range(len(arr) - 1):
        result.append(arr[i])
        result.extend(foo(arr[i], arr[i + 1]))
    result.append(arr[-1])
    return result

result = [[0, 0], [100.0, 0]]

for i in range(n):
    result = bar(result)

for ret in result:
    print("{} {}".format(ret[0], ret[1]))

