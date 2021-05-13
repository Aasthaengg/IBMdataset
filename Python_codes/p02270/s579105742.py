N, K = map(int, input().split())
W = [int(input()) for i in range(N)]


def num_v(p):
    v, kp, vp = 0, 1, 0
    for i in range(N):
        while vp + W[i] > p:
            kp += 1
            vp = 0
            if kp > K:
                break

        else:
            vp += W[i]
            v += 1
            continue

        break

    return v


def main():
    left, right = 0, sum(W)

    while left < right:
        mid = (left+right) // 2
        v = num_v(mid)

        if v == N:
            right = mid
        else:
            left = mid + 1

    print(left)


if __name__ == '__main__':
    main()

