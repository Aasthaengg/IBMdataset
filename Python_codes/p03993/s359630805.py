def main():
    rabbits = int(input())
    like = list(map(int, input().split()))
    answer = 0
    for i in range(rabbits):
        if like[like[i] - 1] == i + 1:
            answer += 1
    print(answer // 2)


if __name__ == '__main__':
    main()

