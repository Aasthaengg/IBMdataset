import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import chain
from copy import deepcopy
def main():
    h, w = map(int, input().split())
    # '#'を1に、'.'を-1に置き換える。
    # 上下左右にダミーのマスとして0を置く。
    hw = []
    hw.append([0] * (w + 2))
    for _ in range(h):
        row = list(input())
        row2 = [-1 if i == '#' else 0 for i in row]
        row3 = list(chain([0], row2, [0]))
        hw.append(row3)
    hw.append([0] * (w + 2))
    hw2 = deepcopy(hw)
    for i1 in range(1, h + 1):
        for i2 in range(1, w + 1):
            if hw[i1][i2] == 0:
                bombs = sum(hw[i1 - 1][i2-1:i2+2])
                bombs += sum(hw[i1][i2 - 1:i2 + 2])
                bombs += sum(hw[i1 + 1][i2 - 1:i2 + 2])
                hw2[i1][i2] = - bombs
    for j1 in range(1, h + 1):
        row4 = hw2[j1][1:w+1]
        row5 = ['#' if i == -1 else str(i) for i in row4]
        print("".join(row5))


if __name__ == '__main__':
    main()