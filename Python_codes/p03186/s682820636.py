x = [int(i) for i in input().split()]
if x[0] + x[1] + 1 >= x[2]:
    ans = x[1] + x[2]
else:
    ans = x[0] + x[1] + 1 #毒入りの枚数
    ans += x[1]
print(ans)