N = int(input())
# 初回は単純に人数として加算
T, A = map(int, input().split())

for _ in range(N - 1):
    t_i, a_i = map(int, input().split())

    # 比率を考えると総人数は T, A = n*t_i, n*a_i の形になる
    # 必ず現在のT, A以上となるnの値を考える
    n = max(-(-T // t_i), -(-A // a_i))

    # 更新
    T, A = n * t_i, n * a_i

print(T + A)