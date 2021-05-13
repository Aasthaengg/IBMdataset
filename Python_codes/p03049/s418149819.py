import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    cnt_BA = cnt_A = cnt_B = cnt_AB = 0
    for _ in range(n):
        s = input().rstrip()
        cnt_AB += s.count("AB")

        if s[0] == "B" and s[-1] == "A":
            cnt_BA += 1
        elif s[0] == "B":
            cnt_B += 1
        elif s[-1] == "A":
            cnt_A += 1

    res = cnt_AB + max(0, (cnt_BA - 1)) + min(cnt_A, cnt_B)
    cnt_BA = 1 if cnt_BA >= 1 else 0
    cnt_A = cnt_A - min(cnt_A, cnt_B)
    cnt_B = cnt_B - min(cnt_A, cnt_B)
    if cnt_A != 0 and cnt_BA != 0:
        res += min(cnt_A, cnt_BA)
    elif cnt_B != 0 and cnt_BA != 0:
        res += min(cnt_B, cnt_BA)
    print(res)


if __name__ == '__main__':
    resolve()
