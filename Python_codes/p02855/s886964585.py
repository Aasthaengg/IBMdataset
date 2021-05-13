def main():
    h, w, k = map(int, input().split())
    cake = [list(input()) for _ in range(h)]
    answer = [[0 for _ in range(w)] for _ in range(h)]
    count = 0
    for i in range(h):
        is_exits_strawberry = False
        for j in range(w):
            if cake[i][j] == "#":
                is_exits_strawberry = True
                count += 1
            if is_exits_strawberry:
                answer[i][j] = count
    for i in range(h):
        if answer[i][-1] == 0:
            continue
        for j in range(-1, -w - 1, -1):
            if answer[i][j] == 0:
                answer[i][j] = answer[i][j + 1]
    for i in range(-2, -h - 1, -1):
        if answer[i][0] == 0:
            answer[i] = answer[i + 1]
    for i in range(1, h):
        if answer[i][0] == 0:
            answer[i] = answer[i - 1]
    for ans in answer:
        print(" ".join(map(str, ans)))


if __name__ == '__main__':
    main()

