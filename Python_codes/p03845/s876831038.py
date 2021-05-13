def main():
    n = int(input())
    times = list(map(int, input().split(' ')))
    n = int(input())
    drinks = [list(map(int, input().split(' '))) for _ in range(n)]
    all_time = sum(times)
    for drink in drinks:
        print(all_time - (times[drink[0]-1] - drink[1]))


if __name__ == '__main__':
    main()