# def bit():
#     S = input()
#     n = len(S) - 1
#     ieS = S[0]
#     for i in range(n):
#         ieS += '*'
#         ieS += S[i+1]
#     ans = 0
#     for i in range(2 ** n):
#         eS = ieS
#         for j in range(n):
#             if (i >> j) & 1:
#                 eS = eS[:(j+1)*2-1] + '+' + eS[(j+1)*2:]
#         ans += eval(eS.replace('*', ''))
#     print(ans)


def solve():
    S = input()
    eS = S[0]
    print(dfs(0, S, eS))


def dfs(i, S, eS):
    if i == len(S)-1:
        return eval(eS)
    return dfs(i+1, S, eS+(S[i+1])) + dfs(i+1, S, eS+'+'+(S[i+1]))


if __name__ == '__main__':
    solve()
