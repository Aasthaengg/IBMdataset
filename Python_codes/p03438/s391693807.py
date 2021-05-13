N = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
a_cnt, b_cnt = 0, 0

for i in range(N):
    # aiをbiに近づける
    if a[i] < b[i]:
        num = (b[i] - a[i] + 1) // 2
        a_cnt += num
        a[i] += 2 * num

for i in range(N):
    # biをaiに近づける
    if b[i] < a[i]:
        b_cnt += (a[i] - b[i])

if a_cnt >= b_cnt:
    print("Yes")
else:
    print('No')