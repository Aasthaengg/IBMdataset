def main():
    N = int(input())
    in_p_list = list(map(int, input().split()))
    p_list = [0 if i+1 == p else 1 for i,p in enumerate(in_p_list)]

    cnt = 0
    for i in range(N-1):
        p1 = p_list[i]
        p2 = p_list[i+1]
        if p1 == 0:
            cnt += 1
            p_list[i] = 1
            p_list[i+1] = 1
    cnt += 1 if p_list[-1] == 0 else 0

    print(cnt)


if __name__ == "__main__":
    main()