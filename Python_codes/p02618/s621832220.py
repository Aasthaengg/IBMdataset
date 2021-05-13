def main():
    from sys import stdin
    input = stdin.readline
    from time import time
    from random import randint
    start = time()
    D = int(input())
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _ in [0]*D]
    ans = [randint(0, 25) for _ in [0]*D]

    def calc_score(ans):
        score = 0
        last = [-1]*26
        for d in range(D):
            ct = ans[d]
            score += s[d][ct]
            last[ct] = d
            for j in range(26):
                score -= c[j]*(d-last[j])
        return score

    score = calc_score(ans)

    while True:
        d = randint(0, D-1)
        new_ct = randint(0, 25)
        past_ct = ans[d]
        ans[d] = new_ct
        new_score = calc_score(ans)
        if new_score > score:
            score = new_score
        else:
            ans[d] = past_ct
        if time() > start+1.8:
            break

    for i in ans:
        print(i+1)


main()
