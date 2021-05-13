n, x = map(int, input().split())
a_list = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    total = a_list[i] + a_list[i+1]
    if total > x:
        diff = total - x
        cnt += diff

        if a_list[i+1] >= diff:
            a_list[i+1] -= diff
        else:
            a_list[i] = diff - a_list[i+1]
            a_list[i+1] = 0
print(cnt)