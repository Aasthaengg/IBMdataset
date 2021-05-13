import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

input_n = lambda: int(readline())
input_nn = lambda: map(int, readline().split())
input_s = lambda: readline().rstrip().decode('utf-8')
input_ss = lambda: readline().rstrip().decode('utf-8').split()


def main():
    N, Q = input_nn()
    S = list(input_s())

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
        l, r = input_nn()
        count = tsum[r] - tsum[l - 1]
        if ac_check[l - 1] == 2:
            count -= 1
        ans.append(count)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
