N = int(input())
a = list(map(int, input().split()))

ans = 0
for i, ai in enumerate(a):
    ai_tmp = ai
    while ai_tmp % 2 == 0:
        ans += 1
        ai_tmp >>= 1

print(ans)