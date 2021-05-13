a,b = map(int,input().split())
ans = 0
for i in range(a,b+1):
    dum = str(i)
    dum_len = len(dum)
    flag = "on"
    for i in range(dum_len//2):
        if dum[i] != dum[-(i+1)]:
            flag = "off"
    if flag == "on":
        ans += 1
print(ans)