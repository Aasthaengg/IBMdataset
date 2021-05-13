import sys


def main():
    N, Q = map(int, input().split())
    S = list(input())
    ac_check = [0] * (N)
    tsum = [0] * (N + 1)

    for i in range(N - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            tsum[i + 2] += 1
            ac_check[i] = 1
            ac_check[i + 1] = 2

    for i in range(N):
        tsum[i + 1] += tsum[i]

    ans = []
    for i in range(Q):
        l, r = map(int, input().split())
        count = tsum[r] - tsum[l - 1]
        if ac_check[l - 1] == 2:
            count -= 1
        ans.append(count)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
