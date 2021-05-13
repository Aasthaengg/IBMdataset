n = int(input())
l_h = list(map(int, input().split()))

max_mov_cnt = 0
tmp = 0
for i in range(n-1):
    if l_h[i] >= l_h[i+1]:
        tmp += 1
    else:
        max_mov_cnt = max(max_mov_cnt, tmp)
        tmp = 0

max_mov_cnt = max(max_mov_cnt, tmp)
print(max_mov_cnt)
