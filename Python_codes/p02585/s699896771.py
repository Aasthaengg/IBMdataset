n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

c_list = []
rink_list = []
visited = set()
ans = -10 ** 10
for i in range(n):
    sum_c = c[i]
    j = p[i] - 1
    num = 1
    while i != j:
        sum_c += c[j]
        j = p[j] - 1
        num += 1

    sum_c = max(0, sum_c)
    # print(f'num:{num}')
    cnt = 1
    j = p[i] - 1
    tmp = c[i]
    ans = max(ans, tmp + sum_c * ((k - cnt) // num))
    while cnt < k and i != j:
        cnt += 1
        tmp += c[j]

        ans = max(ans, tmp + sum_c * ((k - cnt) // num))
        j = p[j] - 1

if ans == 0:
    ans = max(c)

print(ans)