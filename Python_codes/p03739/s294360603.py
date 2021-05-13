n = int(input())
a = list(map(int,input().split()))

cnt = 0
ans1 = 0
for i in range(n):
    cnt += a[i]
    if i % 2 == 1:
        if cnt >= 0:
            ans1 += cnt + 1
            cnt = -1
    else:
        if cnt <= 0:
            ans1 += 1 - cnt
            cnt = 1

cnt = 0
ans2 = 0
for i in range(n):
    cnt += a[i]
    if i % 2 == 1:
        if cnt <= 0:
            ans2 += 1 - cnt
            cnt = 1
    else:
        if cnt >= 0:
            ans2 += cnt + 1
            cnt = -1
            
print(min(ans1,ans2))