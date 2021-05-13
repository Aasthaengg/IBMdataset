import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    """
    まず三角不等式が任意の３頂点に対して成り立つことを確認する。
    なりたってなければグラフは存在しない。

    なりたっている場合は与えられた最短距離と同じ長さの辺を各頂点のペアごとに張れば
    一応条件を満たすグラフは構成できている。

    あとはここから余分な辺をどう削除するかだが、これは三角不等式で統合が成り立っているもの
    として判別できる。
    """

    # 三角不等式チェック
    triangle = True
    used_path = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            minimal_dist = 10**18
            for k in range(N):
                if k == i or k == j: continue
                if A[i][k] + A[k][j] < A[i][j]:
                    triangle = False
                    break
                else:
                    minimal_dist = min(minimal_dist, A[i][k] + A[k][j])
            if A[i][j] < minimal_dist: used_path[i][j] = 1
    if not triangle:
        print(-1)
        return
    
    # 辺の削除
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += A[i][j] * used_path[i][j]
    print(ans)

if __name__ == "__main__":
    main()
