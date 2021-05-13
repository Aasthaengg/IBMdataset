n = int(input())
h = list(map(int, input().split()))
cnt = 0
cnt_tmp = 0
num = h[0]

for i in range(1, n):
    if num >= h[i]:
        cnt_tmp += 1
        num = h[i]
    else:
        num = h[i]
        cnt_tmp = 0
    cnt = max(cnt, cnt_tmp)

print(cnt)