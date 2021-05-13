# https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_c
def main():
    N = int(input())

    for h in range(1, 3500 + 1):
        for n in range(1, 3500 + 1):
            if (4 * h * n - N * n - N * h != 0) and (N * h * n) % (4 * h * n - N * n - N * h) == 0:
                w = (N * h * n) // (4 * h * n - N * n - N * h)
                if w > 0:
                    print(h, n, w)
                    return

if __name__ == "__main__":
    main()