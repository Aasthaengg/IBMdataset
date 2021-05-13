from sys import stdin


def main():
    _ = int(input())
    a_lists = [int(x) for x in stdin.readline().rstrip().split()]
    z = 0

    for a in a_lists:
        z ^= a

    if z == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
