N = int(input())
a = list(map(int, input().split()))
div_cnt = 0
for i in range(N):
    while a[i] % 2 == 0:
        a[i] = a[i] // 2
        div_cnt += 1
print(div_cnt)
