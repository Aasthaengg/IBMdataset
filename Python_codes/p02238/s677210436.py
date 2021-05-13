def dfs(u, colors, matrix, time, detect_time, finished_time):
    # ????????????????????¨??????????????????
    colors = colors
    detect_time = detect_time
    finished_time = finished_time
    time = time + 1
    stack = list()
    stack.append(u)
    colors[u] = 1
    detect_time[u] = time
    while len(stack):
        for i, val in enumerate(matrix[u]):
            if val == 1 and colors[i] == 0:
                time += 1
                stack.append(i)
                colors[i] = 1
                detect_time[i] = time
                u = i
                break
        else:
            time += 1
            e = stack.pop()
            colors[e] = 2
            finished_time[e] = time
            if len(stack):
                u = stack[-1]
    return time


if __name__ == '__main__':
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    color = [0] * N
    for i in matrix:
        node_info = [int(i) for i in input().split()]
        node_i = node_info[0] - 1
        if not node_info[1] == 0:
            for i in node_info[2:]:
                matrix[node_i][i - 1] = 1
    colors = [0] * len(matrix)
    detect_time = [0] * len(matrix)
    finished_time = [0] * len(matrix)
    time = 0
    for i, val in enumerate(colors):
        if val == 0:
            time = dfs(i, colors, matrix, time, detect_time, finished_time)

    for i in range(len(matrix)):
        print('{} {} {}'.format(i + 1, detect_time[i], finished_time[i]))