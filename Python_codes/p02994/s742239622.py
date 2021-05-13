n, l = map(int, input().split())

taste_lists = list()
for i in range(n):
    taste = l+i
    taste_lists.append(taste)

eat = 0
if taste_lists[0] > 0 and taste_lists[-1] > 0:
    eat = taste_lists[0]
elif taste_lists[0] < 0 and taste_lists[-1] < 0:
    eat = taste_lists[-1]
else:
    eat = 0

taste_lists.remove(eat)
ans = 0
for i in taste_lists:
    ans += i

print(ans)