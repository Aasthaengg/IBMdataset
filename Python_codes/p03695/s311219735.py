N = int(input())
a = list(map(int, input().split()))

cnt = [0 for i in range(8)]
count = 0

for i in range(N):
    if 1<= a[i] <= 399:
        cnt[0] = 1
    elif 400<=a[i]<=799:
        cnt[1] = 1
    elif 800<=a[i]<=1199:
        cnt[2] = 1
    elif 1200<=a[i]<=1599:
        cnt[3] = 1
    elif 1600<=a[i]<=1999:
        cnt[4] = 1
    elif 2000<=a[i]<=2399:
        cnt[5] = 1
    elif 2400<=a[i]<=2799:
        cnt[6] = 1
    elif 2800<=a[i]<=3199:
        cnt[7] = 1
    else:
        count += 1

ans_min = sum(cnt)
ans_max = ans_min + count
if ans_min == 0:
    ans_min =1

print("{} {}".format(ans_min, ans_max))