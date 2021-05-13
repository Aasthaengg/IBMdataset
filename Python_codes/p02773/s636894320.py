def main():
    n = int(input())
    s_dict = dict()

    for _ in range(n):
        s = input()
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1

    max_appear = max(s_dict.values())
    lst = []

    for key, value in s_dict.items():
        if value == max_appear:
            lst.append(key)

    lst.sort()

    for s in lst:
        print(s)


if __name__ == "__main__":
    main()
