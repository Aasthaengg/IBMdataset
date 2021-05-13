n = int(input())
p = list(map(int, input().split()))
min_sp, cnt = p[0], 0
for i in range(n):
    if p[i] <= min_sp:
        cnt += 1
        min_sp = p[i]
print(cnt)