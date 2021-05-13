def main():
    height, width, w_min, h_min = map(int, input().split())
    answer = [["1" for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if (i < h_min and j < w_min) or (h_min <= i and w_min <= j):
                answer[i][j] = "0"
    for i in range(height):
        print("".join(answer[i]))


if __name__ == '__main__':
    main()

