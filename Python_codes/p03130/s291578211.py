a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

route_lists = [a1, b1, a2, b2, a3, b3]
cnt_lists = []

for i in range(1, 5, 1):
    cnt = route_lists.count(i)
    cnt_lists.append(cnt)

if 3 in cnt_lists:
    ans = 'NO'
else:
    ans = 'YES'

print(ans)