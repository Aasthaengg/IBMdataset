def min_mp(bls, A, B, C, a_used=False, b_used=False, c_used=False):
    if sum([a_used, b_used, c_used]) == 3:
        return 0
    else:
        min_val = 10**9  # large number
        non_used_num = 3 - sum([a_used, b_used, c_used])
        if len(bls) - 1 >= non_used_num:
            min_val = min([
                min_val,
                min_mp(bls[1:], A, B, C, a_used, b_used, c_used)
            ])
        if len(bls) > 0:
            if not a_used:
                min_val = min([
                    min_val,
                    abs(bls[0] - A) + min_mp(bls[1:], A, B, C, not a_used, b_used, c_used),
                    10 + min_mp(bls[1:], A - bls[0], B, C, a_used, b_used, c_used)
                ])
            if not b_used:
                min_val = min([
                    min_val,
                    abs(bls[0] - B) + min_mp(bls[1:], A, B, C, a_used, not b_used, c_used),
                    10 + min_mp(bls[1:], A, B - bls[0], C, a_used, b_used, c_used)
                ])
            if not c_used:
                min_val = min([
                    min_val,
                    abs(bls[0] - C) + min_mp(bls[1:], A, B, C, a_used, b_used, not c_used),
                    10 + min_mp(bls[1:], A, B, C - bls[0], a_used, b_used, c_used)
                ])
        return min_val


def main():
    N, A, B, C = list(map(int, input().split(' ')))
    bls = [int(input()) for _ in range(N)]  # bamboo length
    print(min_mp(bls, A, B, C))


if __name__ == '__main__':
    main()
