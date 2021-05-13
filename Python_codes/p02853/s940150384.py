X, Y = map(int, input().split())
li = [300000, 200000, 100000]
ans = 0
for i in range(3) :
    if i + 1 == X :
        ans += li[i]
        break

for i in range(3) :
    if i + 1 == Y :
        ans += li[i]
        break
if X == 1 and Y == 1:
    ans += 400000
print(ans)
