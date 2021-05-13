import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    S = input()
    answer = 0
    ans_list = [0]
    for i in range(3):
        if S[i] == "R":
            answer += 1
        if S[i] == "S":
            ans_list.append(answer)
            answer = 0
    ans_list.append(answer)
    print(max(ans_list))


if __name__ == "__main__":
    main()
