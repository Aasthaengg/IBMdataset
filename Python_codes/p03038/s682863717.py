def main():
    from collections import defaultdict
    from operator import itemgetter
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = map(int, input().split())

    ctr = defaultdict(int)
    for x in A:
        ctr[x] += 1

    for _ in range(M):
        num_of_cards, int_written_on_cards = map(int, input().split())
        ctr[int_written_on_cards] += num_of_cards

    rest = N
    total = 0
    for int_written_on_cards, num_of_cards in sorted(ctr.items(), key=itemgetter(0), reverse=True):
        take = min(rest, num_of_cards)

        total += int_written_on_cards * take
        rest -= take

        if rest == 0:
            break

    print(total)


if __name__ == '__main__':
    main()
