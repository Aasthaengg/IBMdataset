
def solve():

    N, A, B, C = map(int, input().split())
    llist = [int(input()) for i in range(N)]
    inf = 10**9

    def dfs(cursol, a, b, c):
        # すべての竹に対して合成魔法を試したら、不足分は延長 or 短縮魔法を使う
        if cursol == N:
            return abs(A-a)+abs(B-b)+abs(C-c)-30 if min(a, b, c) > 0 else inf

        return min(
            dfs(cursol+1, a, b, c),
            # 合成魔法を使っているので+10が必要
            dfs(cursol+1, a+llist[cursol], b, c)+10,
            dfs(cursol+1, a, b+llist[cursol], c)+10,
            dfs(cursol+1, a, b, c+llist[cursol])+10
        )

    print(dfs(0, 0, 0, 0))


if __name__ == "__main__":
    solve()
