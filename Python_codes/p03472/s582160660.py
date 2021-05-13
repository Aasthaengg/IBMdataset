def main():
    N, H = list(map(int, input().split(' ')))
    swords = [list(map(int, input().split(' '))) for _ in range(N)]
    swords.sort(key=lambda s: s[0], reverse=True)
    max_a = swords[0][0]
    throwable_swords = list(filter(lambda s: s[1] > max_a, swords))
    # if len(swords) = 0, then use only the sword with max_a.
    sum_b = sum(list(map(lambda s: s[1], throwable_swords)))
    if H <= sum_b:
        # throw all swords
        throwable_swords.sort(key=lambda s: s[1], reverse=True)
        ans = 0
        for s in throwable_swords:
            ans += 1
            H -= s[1]
            if H <= 0:
                break
        print(ans)
    else:
        # attack with the max_a sword and throw swords
        ans = len(throwable_swords)
        H -= sum_b
        ans += (H + max_a - 1) // max_a
        print(ans)


if __name__ == '__main__':
    main()
