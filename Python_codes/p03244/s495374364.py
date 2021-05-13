import collections

def main():
    n = int(input())
    V = list(map(int, input().split()))
    if len(set(V)) == 1:
        print(n // 2)
        exit()
    evens = []
    odds = []
    for idx, v in enumerate(V, start=1):
        if idx % 2 == 0:
            evens.append(v)
        else:
            odds.append(v)
    c_even = collections.Counter(evens)
    c_odd = collections.Counter(odds)
    even_most_common = c_even.most_common()[0]
    odd_most_common = c_odd.most_common()[0]

    if even_most_common[0] != odd_most_common[0]:
        print(count_replace(c_even, even_most_common[0], c_odd, odd_most_common[0], n))
    else:
        even_second_most_common = c_even.most_common()[1]
        odd_second_most_common = c_odd.most_common()[1]
        vals = []
        vals.append(count_replace(c_even, even_most_common[0], c_odd, odd_second_most_common[0], n))
        vals.append(count_replace(c_even, even_second_most_common[0], c_odd, odd_most_common[0], n))
        print(min(vals))


def count_replace(c_even, even, c_odd, odd, n):
    return n - c_even[even] - c_odd[odd]


if __name__ == '__main__':
    main()
