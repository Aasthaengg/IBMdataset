def solve():
    S = input()
    n = len(S) - 1
    ieS = S[0]
    for i in range(n):
        ieS += '*'
        ieS += S[i+1]
    ans = 0
    for i in range(2 ** n):
        eS = ieS
        for j in range(n):
            if (i >> j) & 1:
                eS = eS[:(j+1)*2-1] + '+' + eS[(j+1)*2:]
        ans += eval(eS.replace('*', ''))
    print(ans)





if __name__ == '__main__':
    solve()
