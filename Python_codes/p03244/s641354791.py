def main():
    n = int(input())
    # n, k = map(int, input().split())
    v = list(map(int, input().split()))
    # s = input()

    even = [0] * (10 ** 5 + 100)
    odd = [0] * (10 ** 5 + 100)

    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1

    max_even = even.index(max(even))
    max_odd = odd.index(max(odd))

    if max_even == max_odd:
        even[max_even] = 0
        odd[max_odd] = 0
        if max(even) < max(odd):
            max_odd = odd.index(max(odd))
        else:
            max_even = even.index(max(even))
    ans = 0
    for i in range(n):
        if i % 2 == 0 and max_even != v[i]:
            ans += 1
        if i % 2 != 0 and max_odd != v[i]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
