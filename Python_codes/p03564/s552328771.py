n = int(input())
k = int(input())
flg = True
ans = 1
for i in range(n):
    if flg:
        if ans * 2 < ans + k:
            ans *= 2
        else:
            ans += k
            flg = False
    else:
        ans += k
print(ans)