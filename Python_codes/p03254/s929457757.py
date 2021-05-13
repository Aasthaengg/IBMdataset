N, x = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

sum = 0
ans = 0
for i in range(len(a)):
    sum += a[i]
    if x >= sum:
        ans += 1
        if ans == N:
            if sum != x:
                ans -= 1
                break
    else:
        break
print(ans)
