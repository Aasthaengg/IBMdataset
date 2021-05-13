from collections import defaultdict


def main():
    counter = defaultdict(int)
    H, W = list(map(int, input().split(' ')))
    for _ in range(H):
        A = input()
        for a in A:
            counter[a] += 1
    if H % 2 == W % 2 == 0:
        # 全ての個数が4の倍数ならOK
        for cnt in counter.values():
            if cnt % 4 != 0:
                print('No')
                return
        print('Yes')
    elif H % 2 == 0 and W % 2 == 1:
        non_quad_chars = 0
        for cnt in counter.values():
            if cnt % 4 == 1 or cnt % 4 == 3:
                print('No')
                return
            elif cnt % 4 == 2:
                non_quad_chars += 1
        if 2 * non_quad_chars <= H and (H - 2 * non_quad_chars) % 4 == 0:
            print('Yes')
        else:
            print('No')
    elif H % 2 == 1 and W % 2 == 0:
        non_quad_chars = 0
        for cnt in counter.values():
            if cnt % 4 == 1 or cnt % 4 == 3:
                print('No')
                return
            elif cnt % 4 == 2:
                non_quad_chars += 1
        if 2 * non_quad_chars <= W and (W - 2 * non_quad_chars) % 4 == 0:
            print('Yes')
        else:
            print('No')
    else:
        center_filled = False
        non_quad_chars = 0
        for cnt in counter.values():
            if cnt % 4 == 1 or cnt % 4 == 3:
                if center_filled:
                    print('No')
                    return
                center_filled = True
                if (cnt - 1) % 4 == 2:
                    non_quad_chars += 1
            elif cnt % 4 == 2:
                non_quad_chars += 1
        if 2 * non_quad_chars <= H + W - 2 and (H + W - 2 - 2 * non_quad_chars) % 4 == 0:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()