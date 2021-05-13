N = int(input())

ans = 0
for i in range(N):
    num = i + 1
    if num % 3 and num % 5:
        ans += num

print(ans)
