N = int(input())
P = [int(input()) for _ in range(N)]

lst = [0] * (N + 1)
for i in range(N):
    lst[P[i]] = i

count = 1
i = 1
while i < N: #startを動かす
    tmp = i
    # print ('tmp', tmp)
    tmp_count = 1
    while tmp < N and lst[tmp] < lst[tmp + 1]:
        tmp_count += 1
        tmp += 1
    count = max(count, tmp_count)
    i = tmp + 1

print (N - count)
# print (lst)