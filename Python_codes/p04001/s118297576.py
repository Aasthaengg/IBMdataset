"""
DFS（深さ優先探索）
"""


def main():
    S = input()
    N = len(S)

    def dfs(i, s):
        if i == N - 1:
            return sum(map(int, s.split('+')))
        return dfs(i + 1, s + S[i + 1]) + dfs(i + 1, s + '+' + S[i + 1])

    print(dfs(0, S[0]))
    return


if __name__ == '__main__':
    main()




