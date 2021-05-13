if __name__ == '__main__':
    N = int(input())
    C = list(input())
    cnt = 0
    red_cnt = 0
    for c in C:
        if c == 'R':
            red_cnt += 1

    for i in range(red_cnt):
        if C[i] == 'W':
            for j in range(red_cnt, N):
                if C[j] == 'R':
                    C[i] = 'R'
                    C[j] = 'W'
                    cnt += 1
                    red_cnt = j+1
    print(cnt)