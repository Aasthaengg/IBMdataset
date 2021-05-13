N = int(input())
l_cnt = [1, 2, 4, 8, 16, 32, 64]
l_ans = [x for x in l_cnt if x <= N]

print((l_ans[-1]))