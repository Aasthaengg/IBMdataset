import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    if N == 1:
        print("Yes")
        print(2)
        print(*[1, 1], sep=" ")
        print(*[1, 1], sep=" ")
        return
    answer = "No"
    for i in range(1, N):
        if (2 * N) % i == 0:
            if (2 * N) // i == i + 1:
                answer = "Yes"
                cnt = i
                break
    print(answer)
    if answer == "No":
        return
    else:
        print(cnt + 1)
        answer = [[] for _ in range(cnt + 1)]
        next_num = 1
        next_place = 1
        while next_num <= N:
            for i in range(cnt + 1):
                if len(answer[i]) < cnt:
                    answer[i].append(next_num)
                    answer[next_place].append(next_num)
                    if len(answer[i]) == cnt:
                        next_place = i + 2
                    else:
                        next_place += 1
                    break
            next_num += 1

        for i in range(cnt + 1):
            ans = [cnt] + answer[i]
            print(*ans, sep=" ")


if __name__ == "__main__":
    main()
