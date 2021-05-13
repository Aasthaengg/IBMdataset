n = int(input())
a = list(map(int, input().split()))
a.sort()
max_num = a[-1] + 1
cnt = [0] * (max_num)
a.sort()
ans = 0


for i in a:
    cnt[i] += 1

a = set(a)

for k in a:
    for l in range(k * 2, (max_num), k):
        cnt[l] += 1

for m in a:
    if cnt[m] == 1:
        ans += 1
    


print(ans)
