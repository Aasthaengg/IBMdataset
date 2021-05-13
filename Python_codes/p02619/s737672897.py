

def inputs():
    D = int(input())
    c = list(map(int, input().split()))
    s = []
    for d in range(D):
        sd = list(map(int, input().split()))
        s.append(sd)
    t = []
    for d in range(D):
        t.append(int(input()))
    return D, c, s, t


def score(D, c, s, t):
    S = 0
    last = [0 for _ in range(26)]
    score_by_day = []

    for day in range(1, D+1):
        ctype = t[day-1]-1
        S += s[day-1][ctype]
        last[ctype] = day

        S -= sum(c[i]*(day-last[i]) for i in range(26))
        score_by_day.append(S)

    return score_by_day


if __name__ == "__main__":
    D, c, s, t = inputs()

    sbd = score(D, c, s, t)
    for sc in sbd:
        print(sc)
