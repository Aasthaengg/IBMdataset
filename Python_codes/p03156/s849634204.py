def main():
    n = int(input())
    a, b = map(int, input().split())
    p_list = list(map(int, input().split()))
    diff_list = [0] * 3

    for p in p_list:
        if p <= a:
            diff_list[0] += 1
        elif a + 1 <= p <= b:
            diff_list[1] += 1
        else:
            diff_list[2] += 1

    print(min(diff_list))


if __name__ == "__main__":
    main()
