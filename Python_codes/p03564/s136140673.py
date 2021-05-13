N = int(input())
K = int(input())

ans = 9999999999

for i in range(2 ** N):
    ans_tmp = 1
    for b in format(i, "0%db" %N):
        if b == "0":
            ans_tmp *= 2
        else:
            ans_tmp += K
    ans = min(ans, ans_tmp)
    
print(ans)