def c_traveling_plan():
    N = int(input())
    # 原点から出発して最後に原点に帰るためこうする (forループも楽)
    A = [0] + [int(i) for i in input().split()] + [0]

    total_tour_cost = sum([abs(A[i] - A[i + 1]) for i in range(N + 1)])
    ans = []
    for i in range(1, N + 1):
        # a_{i-1} -> a_i -> a_{i+1} の長さ(delta1)を引き，
        # a_{i-1} -> a_{i+1} の長さ(delta2)を足す
        delta1 = abs(A[i - 1] - A[i]) + abs(A[i] - A[i + 1])
        delta2 = abs(A[i - 1] - A[i + 1])
        ans.append(total_tour_cost - delta1 + delta2)
    return '\n'.join(map(str, ans))

print(c_traveling_plan())