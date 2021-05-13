from collections import deque


def main():
    N, D, A = map(int, input().split())

    XHN = []
    for _ in range(N):
        X, H = map(int, input().split())
        XHN.append([X, H, X + 2 * D])

    XHN.sort()

    q = deque()
    acc_damege = 0
    ans = 0
    for i in range(N):
        if 0 < XHN[i][1]:
            X, H, bomb_p = XHN[i]

            while q:
                acc_x, acc_d = q[0]
                if acc_x < X:
                    acc_damege -= acc_d
                    del q[0]
                else:
                    break

            H -= acc_damege

            if 0 < H:
                attack_count = H // -A * -1
                damege = A * attack_count
                ans += attack_count
                XHN[i][1] -= damege

                acc_damege += damege
                q.append((bomb_p, damege))

    print(ans)


main()
