import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    P = 10 ** 9 + 7
    num = [0, 0, 0]
    ans = 1
    for a in A:
        cnt = num.count(a)
        if cnt == 0:
            ans = 0
            break
        ans = (ans * cnt) % P
        num[num.index(a)] += 1

    print(ans)


if __name__ == "__main__":
    main()
