def main():
    balls = int(input())
    coordinates = []
    answer = 1
    count_delta = {}
    for _ in range(balls):
        coordinates.append(list(map(int, input().split())))
    coordinates.sort()
    if balls > 1:
        for i in range(balls):
            for j in range(i + 1, balls):
                d = (coordinates[j][0] - coordinates[i][0], coordinates[j][1] - coordinates[i][1])
                if d in count_delta:
                    count_delta[d] += 1
                else:
                    count_delta[d] = 1
        answer = balls - max(count_delta.values())
    print(answer)


if __name__ == '__main__':
    main()

