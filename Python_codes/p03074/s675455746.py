N, K = map(int, input().split())
S = list(input())

prev = S[0]
lst = []
cnt = 1
for s in S[1:]:
    if prev != s:
        lst.append(cnt)
        cnt = 0

    cnt += 1
    prev = s

lst.append(cnt)

right = 0
cnt = 0
l = len(lst)
sum_ = 0
max_ = 0
for i in range(l):
    if S[0] == '0':
        target_cnt = 2 * K + i % 2
    else:
        target_cnt = 2 * K + (i + 1) % 2

    while right < l and cnt < target_cnt:
        sum_ += lst[right]
        cnt += 1
        right += 1

    max_ = max(max_, sum_)
    sum_ -= lst[i]
    cnt -= 1


print(max_)
