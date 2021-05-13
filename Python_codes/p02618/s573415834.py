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
    D = int(input())
    C = [int(c) for c in input().split()]

    S = [0] * D

    for d in range(D):
        S[d] = [int(s) for s in input().split()]

    last = [0] * 26

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
        T[d] = next_t + 1

    for t in T:
        print(t)


if __name__ == "__main__":
    main()
