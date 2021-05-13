from sys import stdin


def main():
    N = int(input())
    a_list = [int(x) for x in stdin.readline().rstrip().split()]
    a_set = set(a_list)

    if len(a_set) == 1:
        if sum(a_set) == 0:
            print("Yes")
        else:
            print("No")

    elif len(a_set) == 2:
        a_1, _2 = sorted(a_set)
        if a_1 == 0:
            if a_list.count(a_1) * 3 == N:
                print("Yes")
            else:
                print("No")
        else:
            print("No")

    elif len(a_set) == 3:
        a_1, a_2, a_3 = a_set
        if a_list.count(a_1) == a_list.count(a_2) and a_list.count(a_2) == a_list.count(a_3):
            if a_1 ^ a_2 == a_3:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")


if __name__ == "__main__":
    main()
