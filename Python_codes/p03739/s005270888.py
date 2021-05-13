def main():
    from itertools import accumulate

    N = int(input())
    *A, = map(int, input().split())
    *acc, = accumulate(A)

    def count(w: int = 1) -> int:
        # m: -+-+-
        # w: +-+-+
        ret = 0
        add_val = 0
        for i, x in enumerate(acc):
            if (i & 1) ^ w:
                b = max(0, 1 - (x + add_val))
                ret += b
                add_val += b

            else:
                b = max(0, (x + add_val) - (-1))
                ret += b
                add_val -= b
        return ret

    ans = min(
        count(w=0),
        count(w=1)
    )

    print(ans)


if __name__ == '__main__':
    main()
