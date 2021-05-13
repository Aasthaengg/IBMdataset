from collections import deque


def solve():
    H, W, N = list(map(int, input().split()))
    # print(H, W, N)

    # 座標は(y, x)
    blacks = {}
    for _ in range(N):
        pos = input().split()
        blacks[(int(pos[0]), int(pos[1]))] = 0

    # print(blacks)

    # [*][*][*]
    # [*][c][*]
    # [*][*][*]
    # ある座標から, それを中心にした9つの座標を返す
    def center_of_boxes_from_point(y, x):
        center_pos_lis = deque()

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                cy = y + dy
                cx = x + dx
                if 1 <= cy <= H and 1 <= cx <= W:
                    center_pos_lis.append((cy, cx))
        return center_pos_lis

    ANS_TABLE = [0 for _ in range(10)]

    # 探索を終了したboxを保存する
    # keyはboxの中心の座標
    done_boxes = {}
    for blk in blacks:
        # print(blk)
        y, x = blk
        boxes = center_of_boxes_from_point(y, x)

        # boxを探索して黒マスをカウントする
        for center_of_box in boxes:
            if center_of_box not in done_boxes:
                y, x = center_of_box
                if 2 <= y < H and 2 <= x < W:
                    count = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            cy = y + dy
                            cx = x + dx
                            if (cy, cx) in blacks:
                                count += 1
                    # print(center_of_box, count)
                    ANS_TABLE[count] += 1
                    done_boxes[center_of_box] = 0

    # print('total boxes', (W - 2) * (H - 2))
    ANS_TABLE[0] = (W - 2) * (H - 2) - sum(ANS_TABLE)

    return ANS_TABLE


if __name__ == '__main__':
    res = solve()
    for r in res:
        print(r)
