n, x = list(map(int, input().split()))
l = list(map(int, input().split()))
cur_d = 0
res = 1
for li in l:
    cur_d += li
    if cur_d > x:
        break
    res += 1
print(res)
