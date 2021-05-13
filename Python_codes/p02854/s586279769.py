# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
# row = [int(input().rstrip()) for _ in range(n)]

def resolve():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())

    a_list = [int(x) for x in input().rstrip().split(" ")]
    length = sum(a_list)
    center = length * 0.5

    # できるだけ中心に近い切れ目
    center_cut = 0
    cut = 0
    for a in a_list:
        cut += a
        if abs(center_cut - center) > abs(cut - center):
            center_cut = cut
        if cut > center:
            break

    # 中心に近い切れ目を中心に一致させる
    print(int(abs(center_cut - center) * 2))


if __name__ == "__main__":
    resolve()
