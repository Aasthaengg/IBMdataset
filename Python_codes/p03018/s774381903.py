def main():
    import sys
    input = sys.stdin.readline
    S = input().strip()
    a_cnt = 0
    state = 0
    ans = 0
    for s in S:
        if s == 'A':
            if state == 0:
                a_cnt += 1
            else:
                a_cnt = 1
                state = 0
        elif s == 'B':
            if state == 0:
                state = 1
            else:
                a_cnt = 0
        elif s == 'C':
            if state == 1:
                ans += a_cnt
                state = 0
            else:
                a_cnt = 0

    print(ans)

if __name__ == '__main__':
    main()
