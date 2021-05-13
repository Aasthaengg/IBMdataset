x = int(input())
ans = x // 11
x -= ans * 11
ans *= 2
if x > 6:
    ans += 2
elif x > 0:
    ans += 1
print(ans)
