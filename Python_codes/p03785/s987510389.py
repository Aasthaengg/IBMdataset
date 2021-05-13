N, C, K = map(int, input().split())  # 人数N, バスの定員C, Ti以上Ti+K以下の時刻に出発するバスに乗らせる必要がある
T = [int(input()) for _ in range(N)]
# print(T)
T.sort()
ans = 1
bus_passengers = 1  # 最大Cまでいける
time_limit = T[0]+K
for i in range(1, N):
    # print(i, ans, time_limit)
    if time_limit >= T[i] and C > bus_passengers:
        bus_passengers += 1
    else:
        # 定員数的に乗りきらないもしくは，時間的に乗れない
        time_limit = T[i]+K
        bus_passengers = 1
        ans += 1
print(ans)
