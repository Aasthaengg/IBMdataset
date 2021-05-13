import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    S = input()
    S = S.replace("BC", "X")
    S = S.replace("C", "B")
    S = S.split("B")
    answer = 0
    for s in S:
        place = []
        c = 0
        n = len(s)
        for i in range(n):
            if s[i] == "A":
                c += 1
                place.append(i + 1)
        for p in place:
            c -= 1
            answer += n - c - p
    print(answer)


if __name__ == "__main__":
    main()
