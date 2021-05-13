def resolve():
    D = int(input())
    C = [int(x) for x in input().split()]
    S = []
    for i in range(D):
        S.append(list(map(int, input().split())))
    last_d = []
    score = 0

    # 各日で満足度が最も増加するコンテストを開催していく(減少は計算しても考慮せず)
    for d in range(D):
        contest = 0
        for i in range(len(C)):  # d日目の最大増加満足度を示すiを探索
            contest = max(contest, S[d][i])
        score += contest
        last_d.append(S[d].index(contest))  # 開催したiを記録
        for i in range(len(C)):
            if i in last_d:
                score -= C[i] * last_d[::-1].index(i)
            else:
                score -= C[i] * (d + 1)
        print(S[d].index(contest) + 1)

    
if __name__ == "__main__":
    resolve()