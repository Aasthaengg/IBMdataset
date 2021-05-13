import sys

if __name__ == '__main__':
    N, K = map(int, input().split())
    xy_list = [list(map(int, input().split())) for i in range(N)]

    all_x = sorted(list(set([xy[0] for xy in xy_list])))
    all_y = sorted(list(set([xy[1] for xy in xy_list])))

    answer = sys.maxsize
    for i in range(len(all_x)):
        x1 = all_x[i]
        for j in range(i+1, len(all_x)):
            x2 = all_x[j]
            for k in range(len(all_y)):
                y1 = all_y[k]
                for l in range(k+1, len(all_y)):
                    y2 = all_y[l]
                    if K <= len([xy for xy in xy_list if (x1 <= xy[0] <= x2) and (y1 <= xy[1] <= y2)]) and answer > (x2-x1) * (y2-y1):
                        answer = (x2-x1) * (y2-y1)

    print(answer)

