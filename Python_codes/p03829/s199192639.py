def main():
    towns, walk_fatigue, teleport_fatigue = map(int, input().split())
    town_location = list(map(int, input().split()))
    answer = 0
    for i in range(towns - 1):
        answer += min(teleport_fatigue, walk_fatigue * (town_location[i + 1] - town_location[i]))
    print(answer)


if __name__ == '__main__':
    main()

