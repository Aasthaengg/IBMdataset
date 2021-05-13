def main():
    n = int(input())
    h_lst = list(map(int,input().split()))
    zero_count = 0
    count = 0

    for i in range(n):

        if h_lst[i] == 0:
            zero_count += 1


    while zero_count < n:

        flag = False
        tmp_count = 0

        for i in range(n):

            if h_lst[i] > 0:
                flag = True
                h_lst[i] -= 1

                if h_lst[i] == 0:
                    zero_count += 1

            else:
                if flag:
                    tmp_count += 1   ## 0でもプラスする必要があるときは、それ以前に0以外の数字があるとき　→　flagで管理
                    flag = False

        if flag:
            tmp_count += 1

        count += tmp_count  ## 一回ごとに足していく

        
    print(count)


if __name__ == '__main__':
    main()