n = int(input())
al = list(map(int,input().split()))

flag = False
before = -1
ans = 0
for a in al:
    if before == a:
        if flag == False:
            ans += 1
            flag = True
        else:
            flag = False
    else:
        flag = False
    before = a
print(ans)