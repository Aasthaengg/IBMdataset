from itertools import accumulate
N, C = map(int, input().split())
Distances, Values = [], []
for i in range(N):
    d, v = map(int, input().split())
    Distances.append(d)
    Values.append(v)

# 右回り・左回りそれぞれのvalue累積(左回りは右回り最後尾が0番目になる)
right_acc_values = list(accumulate(Values))
left_acc_values = list(accumulate(Values[::-1]))

# 右回り・左回りそれぞれのdistance(左回りは右回り最後尾が0番目になる)
right_distances = Distances
left_distances = [C - d for d in Distances[::-1]]

# 右回り・左回りに進んでいった場合に手に入るエネルギー
right_result = [v - d for d, v in zip(right_distances, right_acc_values)]
left_result = [v - d for d, v in zip(left_distances, left_acc_values)]

# 右回り・左回りに進んでいった場合に手に入るエネルギーの累積max
right_result_max = [0]
left_result_max = [0]
for i in range(N):
    right_result_max.append(max(right_result_max[-1], right_result[i]))
    left_result_max.append(max(left_result_max[-1], left_result[i]))


ans = 0
for i in range(N):
    ans = max(ans,
              right_result[i],
              left_result[i],
              right_result[i] + left_result_max[N - i - 1] - right_distances[i],
              left_result[i] + right_result_max[N - i - 1] - left_distances[i])

print(ans)
