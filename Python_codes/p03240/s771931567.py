def search_center(xyh_list):
    xyh_list.sort(key=lambda r: r[2], reverse=True)
    highest = xyh_list[0]
    for cx in range(101):
        for cy in range(101):
            h = highest[2] + abs(highest[0] - cx) + abs(highest[1] - cy)
            matched = True
            for xyh in xyh_list[1:]:
                if xyh[2] == 0:
                    if h - abs(xyh[0] - cx) - abs(xyh[1] - cy) > 0:
                        matched = False
                        break
                else:
                    hh = xyh[2] + abs(xyh[0] - cx) + abs(xyh[1] - cy)
                    if h != hh:
                        matched = False
                        break
            if matched:
                return cx, cy, h
    return None


def main():
    N = int(input())
    xyh_list = [list(map(int, input().split(' '))) for _ in range(N)]
    xyh_list.sort(key=lambda r: r[2], reverse=True)
    cx, cy, ph = search_center(xyh_list)
    print('{} {} {}'.format(cx, cy, ph))


if __name__ == '__main__':
    main()
