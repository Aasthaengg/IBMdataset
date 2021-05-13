def main():
    S = input()
    S_set = set(list(S))
    C_set = set([chr(ord("a") + i) for i in range(26)])

    if len(S_set) == len(C_set):
        S = list(S)
        p = None
        for i in range(len(S) - 2, -1, -1):
            if S[i] < S[i + 1]:
                p = i
                break
        else:
            print(-1)
            return

        ans = S[:p].copy()
        rest = C_set - set(S[: p + 1])
        rest = sorted(rest)
        for r in rest:
            if S[p] < r:
                ans.append(r)
                break
        print(*ans, sep="")
    else:
        diff = C_set - S_set
        diff = sorted(diff)
        print(S + diff[0])
        return


main()
