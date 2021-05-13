N = int(input())
ans = 0
for i in range(1, N+1):
    n = N // i
    temp_sum = n / 2 * (i + n*i)
    ans += int(temp_sum)
print(ans)