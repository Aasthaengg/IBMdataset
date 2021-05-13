def abc106_b():
    n = int(input())
    have_8_divisors = 0

    def count_up_divisor(check_num):
        cnt = 0
        for i in range(1, check_num + 1):
            # 1からcheck_numを順に探索して、nの約数かどうか判断して、約数の時はカウント
            if check_num % i == 0:
                cnt += 1
        return cnt

    for i in range(1, n + 1):
        # 偶数の時はスキップ
        if i % 2 == 0:
            continue

        result = count_up_divisor(i) == 8
        if result:
            have_8_divisors += 1

    print(have_8_divisors)

if __name__ == '__main__':
    abc106_b()