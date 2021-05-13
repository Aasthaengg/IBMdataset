def main():
    house_num = int(input())
    houses = sorted(set(list(map(int, input().split()))))
    print(houses[-1] - houses[0])


if __name__ == '__main__':
    main()

