s = input()
t = input()

s_l = len(s)
t_l = len(t)

ans = len(t)

for i in range(s_l - t_l + 1):
    s_split = s[i:t_l + i] 
   # print(s_split)
    cnt = len(t)
    for j in range(t_l):
        if s_split[j] == t[j]:
            cnt -= 1
    ans = min(ans, cnt)


print(ans)