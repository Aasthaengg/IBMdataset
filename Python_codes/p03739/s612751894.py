def main():
    _ = int(input())
    a = [int(an) for an in input().split()]
    target = {1, -1}
    results = set()
    for sign in target:
        total = 0
        ans = 0
        for an in a:
            total += an
            if sign != ((total > 0) - (total < 0)):
                ans -= (total - sign) * sign
                total = sign
            sign *= -1
        results.add(ans)

    print(min(results))


if __name__ == "__main__":
    main()
