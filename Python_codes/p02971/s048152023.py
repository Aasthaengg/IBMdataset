import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = []
    first = (0, 0)
    sec = 0
    for i in range(N):
        a = int(input())
        A.append(a)
        if first[0] <= a:
            sec = first[0]
            first=(a, i)
        elif sec <a:
            sec =a

    if first[0] == sec:
        for i in range(N):
            print(sec)
    else:
        for i in range(N):
            if i == first[1]:
                print(sec)
            else:
                print(first[0])


if __name__ == "__main__":
    main()
