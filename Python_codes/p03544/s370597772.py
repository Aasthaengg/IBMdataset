n = int(input())
ans = [0] * 87
ans[0] = 2
ans[1] = 1
for i in range(2, n + 1):
    ans[i] = ans[i - 2] + ans[i - 1]
print(ans[n])