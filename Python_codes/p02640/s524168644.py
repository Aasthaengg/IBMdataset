num, leg = map(int, input().split())

ans = "No"
for i in range(num+1):
    leg2 = leg - 4 * i
    if leg2 % 2 == 0 and i + leg2 / 2 == num:
        ans = "Yes"

print(ans)