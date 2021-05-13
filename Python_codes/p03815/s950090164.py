n = int(input())
ans = (n // 11) * 2
mod = n % 11
if mod >= 7: ans += 2
elif 1 <= mod <= 6: ans += 1
print(ans)