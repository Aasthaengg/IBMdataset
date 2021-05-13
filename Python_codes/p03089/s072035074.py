import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    B = [int(x) for x in input().split()]

    ans = []
    while len(ans) < N:
        cnt = 0
        cnti = -1
        for i in range(N):
            if B[i] == 0:
                cnt += 1
            else:
                if B[i] == i - cnt + 1:
                    cnti = i
        if cnti == -1:
            print(-1)
            return
        else:
            ans.append(B[cnti])
            B[cnti] = 0

    for a in ans[::-1]:
        print(a)


if __name__ == '__main__':
    main()
