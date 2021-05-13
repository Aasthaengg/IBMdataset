n = int(input())
a = sorted(list(map(int, input().split())))

ans = a[0]
ans_l = []
ans_e = a[-1]

if ans_e >= 0:
    for i in range(1,n-1):
        if a[i] < 0:
            ans_l += [(ans_e, a[i])]
            ans_e -= a[i]
        else:
            ans_l += [(ans, a[i])]
            ans -= a[i]

    ans_l += [(ans_e,ans)]
    ans = ans_e - ans

else:
    ans = ans_e
    for i in range(0,n-1):
        ans_l += [(ans, a[i])]
        ans -= a[i]

print(ans)

for x, y in ans_l:
    print(x,y)
