def main():
    n = int(input())
    v = [int(_) for _ in input().split()]
    sort_v = sorted(v)

    while len(sort_v) > 1:
        temp_a = sort_v[0]
        temp_b = sort_v[1]
        sort_v.pop(0)
        sort_v[0] = (temp_a + temp_b)/2
        sort_v = sorted(sort_v)

    print(sort_v[0])


if __name__ == "__main__":
    main()
