import collections

def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = collections.Counter(A)
    comb_dict = {}
    for num, freq in c.items():
        comb_dict[num] = freq * (freq-1) // 2
    comb_sum = sum(comb_dict.values())

    ans_dict = {}
    for a in A:
        if a not in ans_dict:
            ans_dict[a] = comb_sum - comb_dict[a] + (c[a] - 1) * (c[a] - 2) // 2
        print(ans_dict[a])


if __name__ == '__main__':
    main()
