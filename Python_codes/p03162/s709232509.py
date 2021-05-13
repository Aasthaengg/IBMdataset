N = int(input())
abc_list = [list(map(int, input().split())) for _ in range(N)]

happy_list = [[0, 0, 0]] # n日目にa|b|cを選んだときの幸福のそこまでの最大値
# before_act = -1 # a: 0, b: 1, c: 2
for n in range(N):
    before_happy_a, before_happy_b, before_happy_c = happy_list[-1]
    a, b, c = abc_list[n]
    tmp_happy_a = max(before_happy_b, before_happy_c) + a
    tmp_happy_b = max(before_happy_c, before_happy_a) + b
    tmp_happy_c = max(before_happy_a, before_happy_b) + c
    happy_list.append([tmp_happy_a, tmp_happy_b, tmp_happy_c])

print(max(happy_list[-1]))