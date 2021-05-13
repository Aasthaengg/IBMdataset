n, p = map(int, input().split())
A = list(map(int, input().split()))

even = 0
odd = 0

for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

ans = 0

if odd == 0:
    if p == 0:
        ans = 2 ** n
    else:
        ans = 0
else:
    ans = 2 ** (n - 1)

print(ans)
