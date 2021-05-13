import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    S = in_s()
    T = in_s()

    SN = len(S)
    TN = len(T)

    ans = []
    for i in range(SN - TN + 1):
        for j in range(TN):
            if S[i + j] == '?' or S[i + j] == T[j]:
                continue
            else:
                break
        else:
            ts = list(S)
            for j in range(TN):
                ts[i + j] = T[j]
            ans.append(ts)

    if len(ans) == 0:
        print('UNRESTORABLE')
    else:
        for i in range(len(ans)):
            ans[i] = ''.join(ans[i]).replace('?', 'a')
        print(sorted(ans)[0])


if __name__ == '__main__':
    main()
