n = int(input())
a = list(map(int, input().split()))
ans = 1
cnt = [3] + [0] * n
for i in a:
    ans *= cnt[i]
    ans %= 10 ** 9 + 7
    if ans == 0:
        break
    cnt[i] -= 1
    cnt[i + 1] += 1
print(ans)