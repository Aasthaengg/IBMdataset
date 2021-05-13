from sys import stdin


def main():
    M_1, D_1 = [int(x) for x in stdin.readline().rstrip().split()]
    M_2, D_2 = [int(x) for x in stdin.readline().rstrip().split()]

    if not M_1 == M_2:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
