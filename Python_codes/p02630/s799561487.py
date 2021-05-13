def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    q = int(input())
    sum_a = sum(a_list)

    a_dict = {}
    for a in a_list:
        if a not in a_dict:
            a_dict[a] = 1
        else:
            a_dict[a] += 1

    for _ in range(q):
        b, c = map(int, input().split())

        if b not in a_dict:
            a_dict[b] = 0
        sum_a += (c - b) * a_dict[b]

        if c not in a_dict:
            a_dict[c] = 0
        a_dict[c] += a_dict[b]
        a_dict[b] = 0

        print(sum_a)


if __name__ == "__main__":
    main()
