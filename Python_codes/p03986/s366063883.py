x = input()
s_cnt = 0
t_cnt = 0
ans = 0
tmp = 0
for s in x:
    if s == "T":
        if tmp == 0:
            ans += 2
        else:
            tmp -= 1
    else:
        tmp += 1
print(ans)