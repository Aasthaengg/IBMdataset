def main():
    N, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    sumA = sum(A)

    def trial_division(n):
        divs = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divs.append(i)
                if i != n//i:
                    divs.append(n//i)
        return divs

    from itertools import accumulate
    divs = trial_division(sumA)
    ans = 0
    for d in divs:
        R = [a % d for a in A if a % d != 0]
        R.sort()
        S = [acc for acc in accumulate(R)]
        M = len(S)
        # print(d, R, S)
        if M == 0:
            ans = max(ans, d)
            continue
        for i in range(M-1):
            ne = S[i]
            po = d*(M-1-i) - (S[M-1] - S[i])
            if po == ne and po <= K:
                ans = max(ans, d)
    print(ans)


if __name__ == '__main__':
    main()
