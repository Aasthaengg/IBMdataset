def main():
    from collections import Counter

    n = int(input())
    *a, = map(int, input().split())

    if n % 3 == 0:
        ctr = Counter(a)
        if len(ctr) == 1:
            print('Yes' if 0 in ctr else 'No')
            return

        elif len(ctr) == 2:
            print('Yes' if ctr[0] == n // 3 else 'No')
            return

        elif len(ctr) == 3:
            x = 0
            p = None
            for k, v in ctr.items():
                if p is None:
                    p = v
                elif p != v:
                    print('No')
                    return
                x ^= k
            print('Yes' if x == 0 else 'No')
            return

        else:
            print('No')
            return

    else:
        print('Yes' if all(map(lambda x: x == 0, a)) else 'No')
        return


if __name__ == '__main__':
    main()
