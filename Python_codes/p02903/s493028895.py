def main():
    H, W, A, B = map(int, input().split())

    lines = [[0 for _ in range(W)] for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if x < A and y < B:
                lines[y][x] = 1
            if x >= A and y >= B:
                lines[y][x] = 1

    for line in lines:
        print("".join(map(str, line)))

if __name__ == '__main__':
    main()
