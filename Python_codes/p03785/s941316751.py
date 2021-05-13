N, C, K = map(int, input().split())
t_li = []
for _ in range(N):
    t_li.append(int(input()))
t_li.sort()
# 最初にバスに乗る乗客の到着時間
first = t_li[0]
# バス1台に乗ってる乗客。最初の一人を載せておく
passengers = 1
# バスの台数。N >= 2なので少なくとも1台は必要
busses = 1
# 二人目から数えていく
for i in range(1, N):
    if passengers < C and t_li[i] - first <= K:
        # 搭乗員数と時間に余裕があるなら、同じバスに乗せていく
        passengers += 1
    else:
        # 次のバスを用意する
        busses += 1
        passengers = 1
        first = t_li[i]
print(busses)
