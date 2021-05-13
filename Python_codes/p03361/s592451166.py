import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    h, w = map(int, input().split())
    # 「黒にするマス」の上下左右にも１つ以上の「黒にするマス」があればOK。
    # '#'を1、'.'を0にする。
    # グリッドの上下左右にダミーマスとして0を置く。
    grid = []
    grid.append([0] * (w + 2))
    for _ in range(h):
        row = list(input())
        row2 = [1 if c == '#' else 0 for c in row]
        grid.append([0] + row2 + [0])
    grid.append([0] * (w + 2))

    for i1 in range(1, h + 1):
        for i2 in range(1, w + 1):
            if grid[i1][i2] == 1:
                black = grid[i1-1][i2] + grid[i1][i2-1] + grid[i1][i2+1] + grid[i1+1][i2]
                if black == 0:
                    print('No')
                    sys.exit()
    print('Yes')

if __name__ == '__main__':
    main()
