x = int(input())
k = x // 11
l = x % 11
ans = 2 * k
if l >= 7:
    ans += 2
elif l >= 1:
    ans += 1
print(ans)