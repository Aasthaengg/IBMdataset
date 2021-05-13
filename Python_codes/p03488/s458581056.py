

def check(goal, dist_data, start):
    dp_now = [0 for i in range(17000)]
    dp_now[start + 8500] = 1
    dp_next = [0 for i in range(17000)]

    for i in range(len(dist_data)):
        for j in range(len(dp_now)):
            if dp_now[j]:
                dp_next[j + dist_data[i]] = 1
                dp_next[j - dist_data[i]] = 1
        dp_now = dp_next
        dp_next = [0 for i in range(17000)]

    return dp_now[goal + 8500]


def main():
    data = input()
    goal = list(map(int, input().split()))
    data = data.split('T')
    move_dist = [len(ele) for ele in data]

    x_data = move_dist[2::2]
    y_data = move_dist[1::2]

    if check(goal[0], x_data, move_dist[0]) and check(goal[1], y_data, 0):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()