n = int(input())
h = [int(i) for i in input().split()]
max_cnt, cnt = 0, 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
print(max(max_cnt, cnt))