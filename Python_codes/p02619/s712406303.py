def main():
    D = int(input())
    C = [int(i) for i in input().split()]
    S = [[int(i) for i in input().split()] for j in range(D)]
    T = [int(input()) for i in range(D)]
    contest_last_opened = [0]*26  # コンテストiを前回開催した日
    score = 0
    for d, t in enumerate(T, start=1):
        get_score = S[d-1][t-1]
        score += get_score
        contest_last_opened[t-1] = d
        loss_score = 0
        for i in range(26):
            ld = contest_last_opened[i]
            loss_score += C[i]*(d-ld)
        score -= loss_score
        print(score)


if __name__ == '__main__':
    main()
