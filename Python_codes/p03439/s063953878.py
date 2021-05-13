import sys
input = sys.stdin.readline


def q(i):
    print(i, flush=True)
    s = input().strip()
    if s == "Vacant":
        exit()
    return s


def f(l, r, lc, rc):
    m = (l+r)//2
    mc = q(m)

    if ((m-l) % 2 and lc == mc) or ((m-l) % 2 == 0 and lc != mc):
        f(l, m, lc, mc)
    elif ((r-m) % 2 and mc == rc) or ((r-m) % 2 == 0 and mc != rc):
        f(m, r, mc, rc)


def main():
    N = int(input())
    lc = q(0)
    rc = q(N-1)
    f(0, N-1, lc, rc)


if __name__ == '__main__':
    main()
