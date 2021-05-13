N, D = map(int, input().split())

can_see = 2*D + 1

ans = int(N / can_see)

if N%can_see != 0:
    ans += 1

print(ans)