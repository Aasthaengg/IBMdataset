n = int(input())
a = list(map(int, input().split()))
a.sort()

cum = [0] * (n + 1)

for i in range(1, n + 1):
    cum[i] = cum[i - 1] + a[i - 1]

ans = 1

for i in range(n, 0, -1):
    if cum[i - 1] * 3 >= cum[i]:
        ans += 1
    else:
        break

print(ans)
