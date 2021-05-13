import copy
import random
import time


memo = {}
def down(d, last, c):
    result = 0
    if d in memo:
        return memo[d]
    for i in range(26):
        result += c[i] * (d - last[i])
    memo[d] = result
    return result


def calc_score_of_the_day(S, d, t, last, C):
    return S[d][t] - down(d+1, last, C) + C[t] * (d+1 - last[t])


def main():
    start = time.time()
    D = int(input())
    C = [int(c) for c in input().split()]

    S = [0] * D

    for d in range(D):
        S[d] = [int(s) for s in input().split()]

    last = [0] * 26
    scores = [float('-inf')] * D

    result = 0
    T = [0] * D
    for d in range(D):
        next_t = 0
        score = float('-inf')
        for t in range(26):
            s = calc_score_of_the_day(S, d, t, last, C)
            if s > score:
                score = s
                next_t = t
        last[next_t] = d + 1
        result += score
        scores[d] = result
        T[d] = next_t + 1


    while time.time() - start < 1.9:
        result = scores[D-1]
        change_date = random.randint(0, D-1)
        change_from = T[change_date]
        change_to = random.randint(1, 26)
        delta = result - scores[change_date-1] if change_date > 0 else result

        if change_from == change_to:
            continue
        copied_T = copy.copy(T)
        copied_T[change_date] = change_to

        delta_to = 0
        last_of_the_day = [t if t <=change_date else 0 for t in last]
        copied_scores = copy.copy(scores)
        for d in range(change_date, D):
            t = copied_T[d] - 1
            score = calc_score_of_the_day(S, d, t, last_of_the_day, C)
            last_of_the_day[t] = d + 1
            delta_to += score
            copied_scores[d] = copied_scores[d-1] + delta_to
            copied_T[d] = t + 1
        if delta_to >= delta:
            scores = copied_scores
            T = copied_T


    for t in T:
        print(t)


if __name__ == "__main__":
    main()
