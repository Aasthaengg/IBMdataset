def main():
    n = int(input())
    s_list = sorted([int(input()) for _ in range(n)])

    sum_s=sum(s_list)
    if sum_s % 10 != 0:
        print(sum_s)
    else:
        for s in s_list:
            if s % 10 != 0:
                print(sum_s - s)
                break
        else:
            print(0)


if __name__ == "__main__":
    main()
