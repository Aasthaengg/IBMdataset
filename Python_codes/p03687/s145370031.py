s = input()
a = "qwertyuiopasdfghjklzxcvbnm"
mi = 100
for i in a:
    ma,cnt = 0,0
    for j in s:
        if j != i:
            cnt += 1
        else:
            ma = max(ma, cnt)
            cnt = 0
        ma = max(ma,cnt)
    mi = min(mi,ma)
print(mi)