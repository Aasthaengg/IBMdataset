import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    A = []
    A.append(int(input()))

    A.append(int(input()))

    A.append(int(input()))

    A.append(int(input()))

    A.append(int(input()))

    k = int(input())


    if A[4]-A[0] >k:
        print(":(")
    else:
        print("Yay!")

if __name__ == "__main__":
    main()
