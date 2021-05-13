n = int(input())
s = input()

ans = 0

for i in range(n):
    one = s[0:i]
    other = s[i:]
    now = 0
    one = set(one)

    for j in one:
        for k in other:
            if j == k:
                now += 1
                break

    ans = max(now, ans)

print(ans)