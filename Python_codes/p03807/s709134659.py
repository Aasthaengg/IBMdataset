n = int(input())
a = list(map(int, input().split()))
odd = 0

for i in a:
    if i % 2 == 1:
        odd += 1

ans = "NO"
if odd % 2 == 1:
    ans = "NO"
else:
    ans = "YES"

print(ans)
