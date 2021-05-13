n = int(input())
numbers = sorted(map(int, input().split()), reverse=True)
ans = 1
for i in numbers:
    ans *= i
    if ans > 10**18:
        ans = -1
        break
if 0 in numbers:
    ans = 0
print(ans)
