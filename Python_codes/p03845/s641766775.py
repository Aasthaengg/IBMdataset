def main():
    n = int(input())
    t_list = list(map(int, input().split()))
    m = int(input())
    total_time = sum(t_list)

    for _ in range(m):
        p, x = map(int, input().split())
        diff = t_list[p - 1] - x
        print(total_time - diff)


if __name__ == "__main__":
    main()
