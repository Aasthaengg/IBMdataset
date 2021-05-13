MOD = 10**9 + 7


def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    from collections import Counter
    c = Counter()
    for a in A:
        s = "{:0>63b}".format(a)[::-1]
        for i, s in enumerate(s):
            c[i] += int(s)
    ans = sum(A) * (N-1)
    for k, v in c.items():
        if v > 1:
            ans -= 2*(2**k)*(v*(v-1)//2)
    print(ans % MOD)


if __name__ == '__main__':
    main()
