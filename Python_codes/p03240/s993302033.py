def main():
    points = int(input())
    info = []
    for _ in range(points):
        info.append(list(map(int, input().split())))
    info.sort(key=lambda x: x[2], reverse=True)
    is_answered = False
    for x in range(101):
        if is_answered:
            break
        for y in range(101):
            now_height = abs(x - info[0][0]) + abs(y - info[0][1]) + info[0][2]
            if all(info[i][2] == max(now_height - abs(x - info[i][0]) - abs(y - info[i][1]), 0) for i in range(1, points)):
                if now_height > 0:
                    print(x, y, now_height)
                    is_answered = True
                    break


if __name__ == '__main__':
    main()