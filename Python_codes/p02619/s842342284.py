def resolve():
    d = int(input())
    ci = list(map(int, input().split()))
    si = []
    for _ in range(d):
        si.append(list(map(int, input().split())))
    answers = [int(input()) for _ in range(d)]

    # 和の計算
    score_now = 0

    # コンテストごとの最後の実行日
    last_dates = [-1]*26
    for date in range(d):
        answer = answers[date]
        score_now += si[date][answer-1]

        last_dates[answer-1] = date
        for c, last_date in zip(ci, last_dates):
            score_now -= c*(date - last_date)
        print(score_now)
resolve()