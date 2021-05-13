x = int(input())
ans = x // 11 * 2
x %= 11
l = [0] + [1] * 6 + [2] * 5
ans += l[x]
print(ans)