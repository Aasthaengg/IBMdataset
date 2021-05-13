def main():
    N = int(input())
    p_list = [list(map(int, input().split())) for i in range(N)]

    z_list = []
    w_list = []
    for i in range(N):
        x = p_list[i][0]
        y = p_list[i][1]
        z_list.append(x + y)
        w_list.append(x - y)
    ans = max(max(z_list) - min(z_list), max(w_list) - min(w_list))
    print(ans)
    return


if __name__ == '__main__':
    main()