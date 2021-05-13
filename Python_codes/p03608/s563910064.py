from itertools import permutations as p


INF = float('inf')
N, M, R = map(int, input().split())
r = list(map(lambda x:int(x) - 1, input().split()))

# 隣接行列
dist = [[INF] * N for _ in range(N)]

# 初期化、対角成分は0、それ以外はINF
for i in range(N):
    dist[i][i] = 0

# 繋がっている街への距離を記録
for _ in range(M):
    A, B, C = map(int, input().split())
    A, B = A - 1, B - 1
    dist[A][B] = dist[B][A] = C


# Warshall-Floyd
def main():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    ans = INF
    # rの全ての並び替えに対して、スタートからゴールまでのdistを足し合わせて最小を求める
    for combi in p(r, R):
        temp = 0
        for i in range(R - 1):
            cost = dist[combi[i]][combi[i + 1]]
            if cost < INF:
                temp += cost
            # 繋がってない場合はbreak
            else:
                break
        else:
            ans = min(ans, temp)

    print(ans)


if __name__ == "__main__":
    main()