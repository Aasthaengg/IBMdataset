import sys

read = sys.stdin.read
readline = sys.stdin.readline
INF = 1 << 60


def main():
    H, W, K = map(int, readline().split())
    S = read().split()

    ans = INF

    for bit in range(1 << (H - 1)):
        idx = [0] * H
        for i in range(H - 1):
            if bit & (1 << i):
                idx[i + 1] = idx[i] + 1
            else:
                idx[i + 1] = idx[i]

        res = idx[-1]
        n = idx[-1] + 1
        A = [0] * n

        for j in range(W):
            B = [0] * n
            ok = True
            for i in range(H):
                if S[i][j] == '1':
                    B[idx[i]] += 1
                    if B[idx[i]] > K:
                        ok = False
                        break

            if not ok:
                res = INF
                break

            divided = False
            for k in range(n):
                A[k] += B[k]
                if A[k] > K:
                    divided = True
                    break

            if not ok:
                res = INF
                break
            if divided:
                A = B
                res += 1

        if ans > res:
            ans = res

    print(ans)
    return


if __name__ == '__main__':
    main()
