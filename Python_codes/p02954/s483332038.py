s = input()
n = len(s)
res = [0]*n
prev = "R"
now_R = 1
cnt = 1
prev_point = 0
for i in range(1,n):
    cur = s[i]
    if now_R:
        if cur =='L' and prev=='R':
            if cnt%2 == 0:
                res[i-1] += cnt//2
                res[i] += cnt//2
            else:
                res[i-1] += cnt//2+1
                res[i] += cnt//2
            prev_point = i
            cnt = 1
            now_R = 0
        else:
            cnt += 1
    else:
        if cur == 'R':
            if cnt%2 == 0:
                res[prev_point-1] += cnt//2
                res[prev_point] += cnt//2
            else:
                res[prev_point-1] += cnt//2
                res[prev_point] += cnt//2+1
            cnt = 1
            now_R = 1
        else:
            cnt += 1
    prev = s[i]
if cnt % 2 == 0:
    res[prev_point - 1] += cnt // 2
    res[prev_point] += cnt // 2
else:
    res[prev_point - 1] += cnt // 2
    res[prev_point] += cnt // 2 + 1
print(*res)