s = input()
if len(set(s)) == 1:
    print(0)
    exit()

alpha = "abcdefghijklmnopqrstuvwxyz"
ans = float("inf")
for tar in alpha:
    t = s
    cnt = 0
    flag = True
    while flag:
        nt = ""
        cnt += 1
        flag = False
        for i in range(len(t)-1):
            if t[i] == tar or t[i+1] == tar:
                nt += tar
            else:
                nt += t[i]
                flag = True
        t = nt
    ans = min(ans, cnt)
print(ans)