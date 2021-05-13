def main():
    slimes = int(input())
    color = list(input().split()) + ["-1"]
    before = color[0]
    count = 1
    answer = 0
    for i in range(1, slimes + 1):
        if before == color[i]:
            count += 1
        else:
            before = color[i]
            answer += count // 2
            count = 1
    print(answer)


if __name__ == '__main__':
    main()

