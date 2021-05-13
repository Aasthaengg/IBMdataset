s = input()

left = 0
ans = 0

for x in s:
    if x == 'B':
        left += 1
        continue
    ans += left

print(ans)
