def main():
    n = int(input())
    p_lst = list(map(int, input().split()))
    count = 0

    for i in range(1, n-1):
        p1 = p_lst[i-1]
        p2 = p_lst[i]
        p3 = p_lst[i+1]
        p123_lst = [p1, p2, p3]
        sorted_lst = sorted(p123_lst)

        if p2 == sorted_lst[1]:
            count += 1

    print(count)

if __name__ == '__main__':
    main()