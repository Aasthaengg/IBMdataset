#!python3

LI = lambda: list(map(int, input().split()))

# input
S = input()

MOD = 10 ** 9 + 7


def main():
    n = len(S)
    m = 5
    w = []
    p = 1
    for i in range(n):
        s = S[-1 - i]
        if s == "?":
            w.append(p)
        else:
            m = (m - int(s) * p) % 13
        p = p * 10 % 13

    n = len(w)
    l1 = [0] * 13
    l1[0] = 1
    for i in range(1, n + 1):
        l2 = [0] * 13
        for j in range(10):
            x = w[i - 1] * j % 13
            for k in range(13):
                t = (x + k) % 13
                l2[t] += l1[k]
        l1 = [y % MOD for y in l2]
    
    ans = l1[m]
    print(ans)


if __name__ == "__main__":
    main()
