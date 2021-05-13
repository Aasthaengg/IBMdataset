n = int(input())
p = [int(input()) for _ in range(n)]

q = [n for _ in range(n)]
for i in range(n):
    q[p[i] - 1] = i

stay_num_cnt = 0
cnt = 0
t = 0
for x in q:
    if x >= t:# x == tはあり得ない
        cnt += 1
    else:
        cnt = 1
    t = x
    stay_num_cnt = max(stay_num_cnt, cnt)
print(n - stay_num_cnt)#, q)