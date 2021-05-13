def main():
    n = int(input())
    lst = [[0, 0, 0]]
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    flag = True
    for i in range(n):
        left_time = lst[i + 1][0] - lst[i][0]
        distance = abs(lst[i + 1][1] - lst[i][1]) + abs(lst[i + 1][2] - lst[i][2])

        if left_time < distance:
            flag = False
            break
        else:
            if left_time % 2 == 0:
                if distance % 2 == 0:
                    continue
                else:
                    flag = False
                    break
            else:
                if distance % 2 == 1:
                    continue
                else:
                    flag = False
                    break

    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()