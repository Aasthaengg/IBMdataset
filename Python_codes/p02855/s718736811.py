import sys
input = sys.stdin.readline


def main():
    H, W, K = map(int, input().split())
    cake = [[0]*W for _ in range(H)]
    sb = []
    for y in range(H):
        s = input().strip()
        for x, c in enumerate(s):
            if c == "#":
                sb.append((y, x))
    for i, (y, x) in enumerate(sb):
        cake[y][x] = i + 1

    for i, s in enumerate(sb):
        i += 1
        y = s[0]
        x0 = x1 = s[1]
        for x in range(s[1]-1, -1, -1):
            if cake[y][x] != 0:
                break
            cake[y][x] = i
            x0 = x
        for x in range(s[1]+1, W):
            if cake[y][x] != 0:
                break
            cake[y][x] = i
            x1 = x
        for y in range(s[0]-1, -1, -1):
            if cake[y][x0:x1+1].count(0) != x1-x0+1:
                break
            for x in range(x0, x1+1):
                cake[y][x] = i
        for y in range(s[0]+1, H):
            if cake[y][x0:x1+1].count(0) != x1-x0+1:
                break
            for x in range(x0, x1+1):
                cake[y][x] = i
    for c in cake:
        print(*c)


if __name__ == '__main__':
    main()
