import sys

sys.setrecursionlimit(1000000)


def main():
    s = input()

    ls = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
    for x in ls:
        if x in s:
            print("Yes")
            return
    print("No")


main()
