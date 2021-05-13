n, p = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for num in a:
    if num % 2 == 1:
        cnt += 1

ans = 0
if cnt == 0:
    if p % 2 == 0:
        ans = 2**n
else:
    ans = 2**(n - 1)

print(ans)