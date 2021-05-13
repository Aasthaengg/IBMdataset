def main():
    # 文字列の入力
    sr = input()

    rc_cnt = 0
    rc_ans = 0

    for s in sr:
        if (s == 'S'):
            rc_cnt = 0
        elif (s == 'R'):
            rc_cnt = rc_cnt + 1
            if (rc_cnt > rc_ans):
                rc_ans = rc_cnt
    
    print(rc_ans)


if __name__ == '__main__':
    main()
