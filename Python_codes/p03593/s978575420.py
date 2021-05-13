import sys
from string import ascii_lowercase as AL

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())

    alpha = {}
    for al in AL:
        alpha[al] = 0
    for i in range(H):
        a = input().rstrip()
        for s in a:
            alpha[s] += 1

    values = list(alpha.values())

    q_h, r_h, = divmod(H, 2)
    q_w, r_w, = divmod(W, 2)
    g_4 = q_h * q_w
    g_2 = q_h * r_w + q_w * r_h
    g_1 = r_h * r_w

    for i in range(len(values)):
        while g_4 > 0:
            if values[i] >= 4:
                g_4 -= 1
                values[i] -= 4
            else:
                break
    for i in range(len(values)):
        while g_2 > 0:
            if values[i] >= 2:
                g_2 -= 1
                values[i] -= 2
            else:
                break
    for i in range(len(values)):
        while g_1 > 0:
            if values[i] == 1:
                g_1 -= 1
                values[i] = 0
            else:
                break

    if g_4 == g_2 == g_1 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
