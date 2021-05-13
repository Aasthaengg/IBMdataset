# D - equeue
def main():
    N, K, *V = map(int, open(0).read().split())
    lim = min(N, K)
    available_choices = set()

    for l in range(lim + 1):
        for r in range(lim + 1):
            if l + r > lim:
                break

            choice = V[:l] + V[-r:] if r else V[:l]
            choice.sort()
            cnt_negatives, cnt_rest = sum(i < 0 for i in choice), K - (l + r)

            if cnt_negatives > cnt_rest:
                available_choices.add(sum(choice[cnt_rest:]))
            else:
                available_choices.add(sum(choice[cnt_negatives:]))

    print(max(available_choices))


if __name__ == "__main__":
    main()
