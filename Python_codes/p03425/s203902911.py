n = int(input())
s = list(input() for _ in range(n))

cnt = [0] * 5

for x in s:
    if x[0] == 'M':
        cnt[0] += 1
    if x[0] == 'A':
        cnt[1] += 1
    if x[0] == 'R':
        cnt[2] += 1
    if x[0] == 'C':
        cnt[3] += 1
    if x[0] == 'H':
        cnt[4] += 1

if cnt.count(0) > 2:
    print(0)
    exit()

ans = 0 
for i in range(len(cnt)-2):
    for j in range(i+1, len(cnt)-1):
        for k in range(j+1, len(cnt)):
            ans += cnt[i] * cnt[j] * cnt[k]

print(ans)
