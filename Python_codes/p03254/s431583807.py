N, x = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])

ans = 0

if sum(a) < x:
  	ans = N - 1
elif sum(a) == x:
    ans = N
else:
    for i in range(N):
        if x >= a[i]:
            x -= a[i]
            ans += 1

print(ans)