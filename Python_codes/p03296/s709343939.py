def slove():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = list(map(int, input().rstrip('\n').split()))
    cnt = 1
    t_cnt = 0
    for i in range(1, n):
        if a[i] != a[i-1]:
            t_cnt += (cnt // 2)
            cnt = 1
        else:
            cnt += 1
    t_cnt += (cnt // 2)
    print(t_cnt)


if __name__ == '__main__':
    slove()
