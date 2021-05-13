n = int(input())
p = list(map(int, input().split()))
min_sp, cnt = p[0], 0
for pi in p:
    if pi <= min_sp:
        cnt += 1
        min_sp = pi
print(cnt)