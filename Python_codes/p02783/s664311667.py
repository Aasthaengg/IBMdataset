import math


def main():
    hp, attack = (int(i) for i in input().rstrip().split(' '))
    ans = str(math.ceil(hp / attack))
    print(ans)


if __name__ == '__main__':
    main()
