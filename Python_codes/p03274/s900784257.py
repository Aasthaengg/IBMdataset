n, k = map(int, input().split())
x = list(map(int, input().split()))

minus = [0]
plus = [0]
if 0 in x:
    k -= 1

for i in x:
    if i < 0:
        minus.append(abs(i))
    elif i > 0:
        plus.append(i)
minus.sort()
#print(minus)
#print(plus)
ans = float("inf")
for left in range(len(minus)):
    if 0 <= k-left < len(plus):
        right = k-left
        res = 2*minus[left] + plus[right]
        res = min(res, minus[left] + 2*plus[right])
        ans = min(ans, res)

print(ans)