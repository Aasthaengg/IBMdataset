n = int(input())
a = list(map(int, input().split( )))
###連続区間に分ける

tmp = a[0]
tmp2 = 1
ans = 0
for i in range(1,n):
    if a[i]==tmp:
        tmp2 += 1
    else:
        tmp = a[i]
        ans += tmp2//2
        tmp2 = 1
ans += tmp2//2
print(ans)