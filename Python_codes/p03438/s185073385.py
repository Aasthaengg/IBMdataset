def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    D = [a - b for a, b in zip(A, B)]
    # [0, 0, ..., 0]の数列に対し、「どれかを-2」「どれかを+1」をk回ずつやってDを作れるか？
    cnt_m2 = 0
    cnt_p1 = 0
    # 必要最低限な個数を計算
    for d in D:
        if d < 0:
            if d % 2 == 0:
                cnt_m2 += abs(d) // 2
            else:
                cnt_m2 += (abs(d) + 1) // 2
                cnt_p1 += 1
        elif d > 0:
            cnt_p1 += d
    # 基本的に「-2の回数」==「+1の回数」にできればYes。
    # ちなみに同じ数に対する操作として「-2の回数」:「+1の回数」=1:2 ならプラマイゼロで相殺されるので、
    # 相殺可能な操作を足して「-2の回数」==「+1の回数」にできればYes。
    # つまり cnt_m2 >= cnt_p1 ならYes。
    if cnt_m2 >= cnt_p1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()